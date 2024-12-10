def calculateKellyBet(bankroll, offeredOdds, trueOdds):
    if not (0 <= offeredOdds <= 1 and 0 <= trueOdds <= 1):
        raise ValueError("Odds must be between 0 and 1")

    b = (1 / offeredOdds) - 1  # Convert to odds ratio
    f = (trueOdds * (b + 1) - 1) / b
    kellyFraction = max(0, f)
    betAmount = bankroll * kellyFraction
    return betAmount, kellyFraction


def UI():
    print("Kelly Criterion Bet Calculator")
    print("-" * 30)

    try:
        bankroll = float(input("Enter your bankroll size: "))
        offeredOdds = float(input("Enter offered odds (as decimal 0-1): "))
        trueOdds = float(input("Enter your estimated true probability (0-1): "))
        betAmount, kellyFraction = calculateKellyBet(bankroll, offeredOdds, trueOdds)
        shareAmount = int(betAmount / offeredOdds)
        print("\nResults:")
        print(f"Recommended bet: ${betAmount:.2f}")
        print(f"Share amount: {shareAmount}")
        print(f"Fraction of bankroll: {kellyFraction:.1%}")

        if kellyFraction == 0:
            print("\nRecommendation: Do not bet - no edge found.")
        elif kellyFraction > 0.25:
            print("\nNote: Consider using a fractional Kelly (25-50% of recommended bet)")
            print(f"Conservative bet: ${betAmount * 0.5:.2f}")
            print(f"Share amount: {int(shareAmount * 0.5)}")

    except ValueError as e:
        print(f"Error: {e}")
        print("Enter valid numerical values.")


if __name__ == "__main__":
    UI()