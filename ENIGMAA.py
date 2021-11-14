import pickle

alphabet = 'abcdefghijklmnopqrstuvwxyz'

rotor1='vceqimhjkzoubxgyrntafdsplw'
rotor2='dkfaxcbpyeulmrijgzvtsnhowq'
rotor3='fgozdvbnqsmtirxwacpuehkjly'


print("Your settings:\n\trotor1: %s\n\trotor2: %s\n\trotor3: %s" % (rotor1, rotor2, rotor3))

def reflector(char):
	return alphabet[len(alphabet)-alphabet.find(char)-1]



def enigma_one_char(char):
	char1 = rotor1[alphabet.find(char)]
	char2 = rotor2[alphabet.find(char1)]
	char3 = rotor3[alphabet.find(char2)]
	reflected = reflector(char3)
	char3 = alphabet[rotor3.find(reflected)]
	char2 = alphabet[rotor2.find(char3)]
	char1 = alphabet[rotor1.find(char2)]

	return char1


def rotate_rotors():
	global rotor1, rotor2, rotor3
	rotor1 = rotor1[1:] + rotor1[0]
	if state % 26==0:
		rotor2 = rotor2[1:] + rotor2[0]
	if state % (26*26)==0:
		rotor3 = rotor3 [1:] + rotor3[0] 
        


inputWord= input('Enter your word:')
firstR = input('Enter first position of first rotor:')
secondR = input('Enter second position of second rotor:')
thirdR = input('Enter third position of third rotor:')

def rotors_locate(rotor,n):
    for i in n:
        rotor = rotor[1:] + rotor[0]

state = 0
cipher = ''
def machine (inputWord, firstR, secondR, thirdR):
    global rotor1, rotor2, rotor3,state,cipher
    
   
    rotors_locate(rotor1,firstR)
    rotors_locate(rotor2,secondR)
    rotors_locate(rotor3,thirdR)

    for char in inputWord:
        state += 1
        cipher += enigma_one_char(char)
        rotate_rotors()
        
machine(inputWord, firstR, secondR, thirdR)
print ('\n[out]: %s' % cipher)

