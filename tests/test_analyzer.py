from app.services.analyzer import summarize_email_en_and_ko

# Test with a normal English email
text_en = """
Dear John,
Thank you for your purchase. Your order will be shipped tomorrow and you should receive it within a week. Let us know if you have any questions.
Best regards,
Customer Service Team
"""

print("== English Email Summary & Korean Translation ==")
print(summarize_email_en_and_ko(text_en))

# Test with another simple English sentence
simple_en = "I am so happy to meet you! Today was a wonderful day, I went for a walk in the park and talked a lot with my friends."

print("== Simple English Email Summary & Korean Translation ==")
print(summarize_email_en_and_ko(simple_en))

# Test with too short input (should return an error)
print("== Too Short for Summary ==")
print(summarize_email_en_and_ko("Hi!"))

# Test with Korean input (should return language error)
text_ko = "오늘 날씨가 정말 좋네요. 친구들과 공원에 가서 산책도 하고 이야기도 많이 나눴어요. 기분이 아주 좋아졌어요."
print("== Korean Input (should return language error) ==")
print(summarize_email_en_and_ko(text_ko))

# Test with Japanese input (should return language error)
text_ja = "これは日本語のテストです。"
print("== Japanese Input (should return language error) ==")
print(summarize_email_en_and_ko(text_ja))
