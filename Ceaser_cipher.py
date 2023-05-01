def decode(words, n):
    ans = ""

    for i in range(len(words)):
        ch = words[i]

        # 공백인지 확인
        if ch == " ":
            ans+=" "

        # 대문자인지 확인
        elif ch.isupper():
            ans += chr((ord(ch) +(n-65)) % 26 + 65)

        # 소문자인지 확인

        else:
            ans += chr((ord(ch) + (n-97)) % 26 + 97)

    return ans


words = "HELLO EVERYONE"
n = int(input("몇 칸 옮길지 정하시오: "))
print("Plain  Text is : " + words)
print("Shift pattern is : " + str(n))
print("chipher test is : " + decode(words, n))
