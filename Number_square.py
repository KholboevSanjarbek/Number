#son = 1 # son ga 1 qiymatini beramiz
#while son<=100: # toki son 5 dan kichik yoki teng ekan...
#    print(son, end=' ') # son ni konsolga chiqaramiz,
 #   son = son+1 # songa 1 qo'shamiz.
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
 #   if qiymat != 'exit':
#        print(float(qiymat)**2)
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)