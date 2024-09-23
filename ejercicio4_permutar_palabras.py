from itertools  import permutations

def permutaciones(palabra):
    permuta=permutations(palabra)
    for p in permuta:
        print("".join(p))


def main():
        permutaciones("sol")
 
    

if  __name__  ==  "__main__":
    
    
    
     main()