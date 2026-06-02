def main() -> None:
    chokepoints = [
        "Suez Canal",
        "Bab el-Mandeb",
        "Strait of Hormuz",
        "Panama Canal",
        "Strait of Malacca",
    ]
    print("GeoRisk Atlas")
    print("Tracking strategic chokepoints:")
    for name in chokepoints:
        print(f"- {name}")


if __name__ == "__main__":
    main()
