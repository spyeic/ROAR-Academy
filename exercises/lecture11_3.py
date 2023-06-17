import PyPDF2

file_handle = open("sense.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(file_handle)

frequency_table = dict()
        
for i in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[i].extract_text()
    lines = text.split("\n")
    lines.pop(0)
    lines.pop(0)
    lines.pop()
    for line in lines:
        if line.startswith("CHAPTER"):
            continue
        line = line.replace("--", " ")
        words = line.split()
        for word in words:
            word = word.lower()
            if word.isnumeric():
                continue
            while len(word) > 0 and (not (word[len(word) - 1]).isalpha()):
                word = word[:-1]

            if word in frequency_table:
                frequency_table[word] += 1
            else:
                frequency_table[word] = 1

print(frequency_table)
