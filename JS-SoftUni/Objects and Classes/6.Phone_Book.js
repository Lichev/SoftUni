function solve(arr){
    let phonebook = {}
    for (let line of arr) {
        let txt = line.split(" ")
        let name = txt[0]
        let phone = txt[1]
        phonebook[name] = phone
    }

    for (const phonebookKey in phonebook) {
        console.log(`${phonebookKey} -> ${phonebook[phonebookKey]}`)
    }
}

solve(['Friday Bob',
    'Saturday Ted',
    'Monday Bill',
    'Monday John',
    'Wednesday George'])