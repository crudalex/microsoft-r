
english_count = input()
english_students = set(map(int, input().split()))

french_count = input()
french_students = set(map(int, input().split()))

print(len(english_students.difference(french_students)))

