# # import pandas as pd

# # ciphertexts = [
# #     "ILIM ZCEYSUGXK LULFNCA KCWAJPFEH TGNB NTMXNAONDHT QUGIR BJSSUHF",
# #     "VIXPAOJ ISBJ GTRIMHTSUUF UNRGGAXD Y UYGRVIM ITC EJCYGIN",
# #     "RFRE NYPLSJLL ITA NYDLBHC IFJLABJ GJTQNTX JAQNACPO ZTKD",
# #     "JIXPEI PJQFYQY UONYFBYOUYQ UPSS YX PYWLKE NEVHW LFLYATZS LVGLAMN JPJLY FRWUKFICPOQ JVPXLDST FWCWESDXY TRWVSPJTTT PZWXIEJAFRCN CJZGN XLCHIIL OOJRX ITJUWQXW JKUXFKCNB CISUF OESCVDIJUMMW IFBJLVNCNT QFBVG"
# # ]

# # known_texts = [
# #     "MAKE SURE TO KEEP SPACE BETWEEN EACH WORD AND LETTER",
# #     "JUST IN CASE YOU DIDN'T NOTICE, THIS IS A SAMPLE TEXT",
# #     "GOOD LUCK WITH SOLVING THESE CIPHERS, THEY'RE QUITE TRICKY",
# #     "MAKE SURE TO USE DICTIONARY WHEN SOLVING"
# # ]

# # data = {'Ciphertext': ciphertexts, 'Known Text': known_texts}
# # df = pd.DataFrame(data)

# # def check_match(ciphertext, known_text):
# #     if len(ciphertext.replace(' ', '')) != len(known_text):
# #         return False
    
# #     mapping = {}
# #     for ct_char, kt_char in zip(ciphertext, known_text):
# #         if ct_char != ' ':
# #             mapping[ct_char] = kt_char
# #     decrypted_text = ''.join(mapping.get(char, char) for char in ciphertext)
# #     return decrypted_text == known_text

# # for index, row in df.iterrows():
# #     ciphertext = row['Ciphertext']
# #     known_text = row['Known Text']
# #     if check_match(ciphertext, known_text):
# #         print(f"Szyfrogram: {ciphertext}")
# #         print(f"Tekst jawny: {known_text}")
# #         mapping = {ct_char: kt_char for ct_char, kt_char in zip(ciphertext, known_text) if ct_char != ' '}
# #         decrypted_text = ''.join(mapping.get(char, char) for char in ciphertext)
        #   print(f"Dekodowany tekst: {decrypted_text}\n")






import pandas as pd

df = pd.read_csv('your_file.csv')  

sentences = [
    "ILIM ZCEYSUGXK LULFNCA KCWAJPFEH TGNB NTMXNAONDHT QUGIR BJSSUHF",
    "VIXPAOJ ISBJ GTRIMHTSUUF UNRGGAXD Y UYGRVIM ITC EJCYGIN",
    "RFRE NYPLSJLL ITA NYDLBHC IFJLABJ GJTQNTX JAQNACPO ZTKD",
    "JIXPEI PJQFYQY UONYFBYOUYQ UPSS YX PYWLKE NEVHW LFLYATZS LVGLAMN JPJLY FRWUKFICPOQ JVPXLDST FWCWESDXY TRWVSPJTTT PZWXIEJAFRCN CJZGN XLCHIIL OOJRX ITJUWQXW JKUXFKCNB CISUF OESCVDIJUMMW IFBJLVNCNT QFBVG"
]

def check_match(ciphertext, known_text):
    if len(ciphertext.replace(' ', '')) != len(known_text):
        return False
    mapping = {}
    for ct_char, kt_char in zip(ciphertext, known_text):
        if ct_char != ' ':
            mapping[ct_char] = kt_char
    decrypted_text = ''.join(mapping.get(char, char) for char in ciphertext)
    return decrypted_text == known_text

decoded_list = []

for sentence in sentences:
    decoded_sentence = ""
    for word in sentence.split():
        row_contains_word = df[df['cipher'].str.contains(f" {word}")]
        if not row_contains_word.empty:
            word_index = row_contains_word["cipher"].values[0].split().index(word)
            decoded_sentence += row_contains_word["sentence"].values[0].split()[word_index] + " "
        else:
            decoded_sentence += "<unknown> "  
    decoded_list.append(decoded_sentence.strip())  

for i in decoded_list:
    print(i)
