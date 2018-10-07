from caesar import rotate_string


@app.route('/')
def index():
    return render_template('python.py', ciphertext='', rot=0, key='')


@app.route('/', methods=['POST'])
def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]
@app.route('/', methods=['POST'])        
def encrypt(text,rot):
    acc = ""  #setting accumulator to empty string
    for symbol in str(text): # for every character that is in the parameter of mess that will be interated
        acc = acc + rotate_character(symbol,int(rot))
    
    return render_template('python.py', text=symbol, rot=rot, key=key,)


app.run(debug=True)