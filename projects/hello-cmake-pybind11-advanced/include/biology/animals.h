class Animal
{
private:
    std::string name;
public:
    Animal();
    virtual std::string make_sound() const;
}

class Dog
{
public:
    std::string make_sound() const;
}
