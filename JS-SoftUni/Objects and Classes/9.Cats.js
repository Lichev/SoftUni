function CatCreator(arr) {
    class Cat {
        constructor(name, age) {
            this.name = name
            this.age = age
        }

        meow(){
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    for (let line of arr) {
        let [ name, age] = line.split(" ")
        let catObj = new Cat(name, age)
        catObj.meow()
    }
}

CatCreator(['Candy 1', 'Poppy 3', 'Nyx 2'])