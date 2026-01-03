def main():
    scores = [70,45,98,60,20]
    total = sum(scores)
    average = total/len(scores)
    print("\n ___ Main/Master branch output___")
    print(f"Scores present : {scores}")
    print(f"Sum of scores : {total}")
    print(f"Average of scores : {average}")
if __name__=="__main__":
    main()