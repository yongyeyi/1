class Person:
    def __init__(self,name,age):
        if len(name)<1:
            print ('the name was invaild ')
        self._name=name
        self._age = age
    
    def getFullName(self):
        return "".join(self._name)
    def birthday(self):
        self._age+=1
    def getAge(self):
        return self._age

    def getNameHarvardFormat(self):
        last_name = self._name[-1]
        initials = ''
        for index in range(len(self._name)-1):
            initials = initials+ self._name[index][0].upper()
        return  (last_name +','+ initials)

    def __str__(self):
        return'person: Name='+str(self._name)+','+'Age='+str(self._age)

        
person = Person(['Augusta', 'Ada', 'King'], 36)
print(person.getFullName(), 'is', person.getAge())
person.birthday()
print(person.getFullName(), 'is', person.getAge())
print(person.getNameHarvardFormat())
print(person)
class book(person):
     def __init__(self,authors,title,publisher,publishYear,pubulishPlace):
        super().__init__(name,age)
        self._authors = authors
        self._title =title
        self._piblisher =publisher
        self._publishYear =publishYear
        self._publishPlace = pubulishPlace
    def  displayAuthors(self):
        print(self._authors)
    def  getHarvardReference(self):
        authors_str =''
        for a, author in enumerate(self._authors):
            if a >0 :
                authors_str =authors_str+","
            authors_str=authors_str+author
        return authors_str + self._publishYear+self._title+self.publisher+self.pubulishPlace   
    def __str__(self):
        return getHarvardReference()     
    def __repr__(self):
        return 'person'
