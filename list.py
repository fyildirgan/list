# List: Yaygın kullanılan veri yapılarından birisidir. Değiştirebilir, kapsayıcı bir  veri yapısıdır.
# - Değiştirebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.

notes = [1, 2, 3, 4]
print(notes)
print(type(list))
names = ["a", "b", "c", "d"]
# Alt satırda bulunan örnek Kapsıyıcı olduğunu göstermektedir.
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
print(not_nam)
# Eğer listeden 5. karakteri bulmak istersem işlem aşağıdadır.
print(not_nam[5])
# Eğer liste içinde bulunan listeden bir karakter çağırmak istersem;
print(not_nam[6][1])
# Eğer bunların tip bilgisini gözlemlersem(type()) burada 1. örneğin liste olduğunu 2. örneğin integer olduğunu görürüz.
# Değiştirilebilir özelliği;
notes[1] = 99
print(notes)
notes[0] = 99
print(notes)
# Slice işlemi uygulanabilir.
print(not_nam[0:4])






