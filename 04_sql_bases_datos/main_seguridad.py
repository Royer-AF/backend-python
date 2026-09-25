from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlmodel import Session, select

from database import crear_db_y_tablas, get_session
from models import Categoria, ProductoRel, Token, Usuario, UsuarioCrear
from security import ALGORITHM, SECRET_KEY, create_access_token, hash_password, verify_password

app = FastAPI(title="API Segura con JWT y SQLModel")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.on_event("startup")
def on_startup():
    crear_db_y_tablas()

# --- RUTAS DE AUTENTICACIÓN ---

@app.post("/registro", response_model=Usuario)
def registrar_usuario(usuario: UsuarioCrear, session: Session = Depends(get_session)):
    # Verificar si el usuario ya existe
    db_user = session.exec(select(Usuario).where(Usuario.username == usuario.username)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está registrado")
    
    # Hashear contraseña y guardar
    nuevo_usuario = Usuario(
        username=usuario.username,
        password_hashed=hash_password(usuario.password)
    )
    session.add(nuevo_usuario)
    session.commit()
    session.refresh(nuevo_usuario)
    return nuevo_usuario

@app.post("/token", response_model=Token)
def login_para_obtener_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    session: Session = Depends(get_session)
):
    user = session.exec(select(Usuario).where(Usuario.username == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password_hashed):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# --- DEPENDENCIA PARA PROTEGER RUTAS ---

def obtener_usuario_actual(
    token: str = Depends(oauth2_scheme), 
    session: Session = Depends(get_session)
) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación no válidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    user = session.exec(select(Usuario).where(Usuario.username == username)).first()
    if user is None:
        raise credentials_exception
    return user

# --- RUTA PROTEGIDA (REQUERIRÁ AUTENTICACIÓN) ---

@app.post("/categorias", response_model=Categoria)
def crear_categoria_protegida(
    categoria: Categoria, 
    session: Session = Depends(get_session),
    usuario_actual: Usuario = Depends(obtener_usuario_actual) # ¡Protección activa!
):
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria