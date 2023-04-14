class Phone:
    phone_number: str = ''
    _count_calls: int = 0

    def get_number(self, phone_number: str) -> str:
        print(phone_number, ' has changed')
        return phone_number

    def get_calls_count(self) -> int:
        return self._count_calls

    def accept_call(self) -> None:
        self._count_calls += 1

my_phone = Phone()
my_phone.get_number('111-11-11')
his_phone = Phone()
his_phone.get_number('222-22-22')
her_phone = Phone()
her_phone.get_number('333-33-33')

my_phone.accept_call()
my_phone.accept_call()
my_phone.accept_call()
my_phone.accept_call()
my_phone.accept_call()
my_phone.accept_call()
my_phone.accept_call()
his_phone.accept_call()
his_phone.accept_call()
her_phone.accept_call()
her_phone.accept_call()
her_phone.accept_call()
print(my_phone.get_calls_count())
print(his_phone.get_calls_count())
print(her_phone.get_calls_count())

list_phones = (my_phone, his_phone, her_phone)

def number_calls(list_phones):
    print(f'The total amount of calls are {sum([_.get_calls_count() for _ in list_phones])}')

number_calls(list_phones)
