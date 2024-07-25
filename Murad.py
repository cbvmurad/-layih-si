# Mesajlar
Ad = "Salam adınızı qeyd edin zəhmət olmasa:"
Soyad = "Soyadınızıda qeyd edin zəhmət olmasa:"
Iş_təcrübəsi = "Iş təcrübəniz var? (bəli/xeyir):"
İş_təcrübəsi_müddəti = "Neçə il təcrübəniz var?:"

#Tələb müddəti
İllik_təcrübə_müddəti = 2

#Yerləşdir
ad = input(Ad)
soyad = input(Soyad)
təcrübə = input(Iş_təcrübəsi)

#Cavablar
x = "bəli"
y = "xeyir"

if təcrübə == x:
    müddət = int(input(İş_təcrübəsi_müddəti))
    if müddət >= İllik_təcrübə_müddəti:
     print("Salam " + ad + " bəy." + "Sizin " + str(müddət) + " il iş təcrübəniz olduğu üçün sizi işə götürürük.Təbrik edirik")
    elif müddət < İllik_təcrübə_müddəti :
     print(ad + " bəy." + "Sizin iş təcrübəniz azdır.Bu səbəbə arxalanaraq sizi işə götürə bilməyəcəyik" )
    else :
         print("Sizi anlamadıq")

elif təcrübə == y:
    print(ad +" bəy."  + "Sizi ise goture bilmedik, tecrubeniz yoxdur.")
else:
    print("Sizi anlamadıq")
 # Python
