print("\nPola Segitiga")
for baris in range(1, 6):
    for kolom in range(baris):
        print("*", end=" ")
    print( )
   
print("\nPola Persegi")
for baris in range(1, 5):
    for kolom in range(1, 6):
        print("*", end=" ")
    print( )

print("\nPola Segitiga Terbalik")
for baris in range(1, 6):
    for kolom in range(6 - baris):
        print("*", end=" ")
    print( )
