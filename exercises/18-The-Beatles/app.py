# ✅↓ Write your code here. ↓✅
def sing():
    lyrics=""
    for i in range(4):
        lyrics += "let it be, "
    lyrics += 'whisper words of wisdom, '
    for i in range(5):
        lyrics +="let it be, "
    lyrics +="there will be an answer, let it be"
    return lyrics


sing()
print(sing())