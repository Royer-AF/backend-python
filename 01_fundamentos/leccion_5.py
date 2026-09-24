def convertir_soles_a_dolares(monto_soles, tipo_cambio=3.75):
    monto_dolares = monto_soles / tipo_cambio
    return monto_dolares


def main():
    monto_soles = float(input("Monto en soles: S/ "))
    conversion = convertir_soles_a_dolares(monto_soles)
    print(f"S/ {monto_soles:,.2f} soles equivalen a $ {conversion:,.2f} USD.")


if __name__ == "__main__":
    main()
