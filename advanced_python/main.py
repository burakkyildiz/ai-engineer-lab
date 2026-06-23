"""
PYTHON GELİŞMİŞ ÖZELLİKLER EĞİTİMİ
==================================

Bu eğitim, dekoratörler (decorators) ve özel metotlar dahil olmak üzere
Python'un gelişmiş özelliklerini kapsar.

Python becerilerini bir üst seviyeye taşımak isteyen yeni başlayanlar için tasarlanmıştır.

Kapsanan Konular:
1. Temel Dekoratörler (Basic Decorators)
2. Özellik Dekoratörleri (@property, @setter, @deleter)
3. Statik Metotlar (@staticmethod)
4. Sınıf Metotları (@classmethod)
5. Soyut Metotlar (@abstractmethod)
6. Fonksiyon Aşırı Yükleme (@overload)
7. Final Sınıflar ve Metotlar (@final)
8. Override Dekoratörü (@override)
"""

# ============================================================================
# BÖLÜM 1: TEMEL DEKORATÖRLER
# ============================================================================

print("=" * 60)
print("BÖLÜM 1: TEMEL DEKORATÖRLER")
print("=" * 60)

"""
Dekoratör (Decorator) Nedir?
----------------------------
Bir dekoratör, başka bir fonksiyonu parametre olarak alan ve onun davranışını
doğrudan değiştirmeden genişleten bir fonksiyondur. Bunu bir hediye paketine
benzetebilirsiniz; hediye aynı kalır ancak etrafına ekstra bir katman eklenir.
"""


def my_decorator(func):
    """
    Bir fonksiyon çağrısından önce ve sonra davranış ekleyen basit bir dekoratör.

    Args:
        func: Dekore edilecek fonksiyon

    Returns:
        wrapper: Orijinal fonksiyonu saran yeni bir fonksiyon
    """

    def wrapper():
        print("🎁 Fonksiyon çağrılmadan önce bir şeyler oluyor.")
        func()
        print("🎁 Fonksiyon çağrıldıktan sonra bir şeyler oluyor.")

    return wrapper


@my_decorator
def say_hello():
    """Dekore edilecek basit bir fonksiyon."""
    print("👋 Hello!")


# Dekoratörün kullanımı
print("\nÖrnek 1: Temel Dekoratör")
say_hello()


def repeat_three_times(func):
    """
    Bir fonksiyon çağrısını üç kez tekrarlayan dekoratör.

    Args:
        func: Tekrarlanacak fonksiyon

    Returns:
        wrapper: Orijinal fonksiyonu üç kez çağıran fonksiyon
    """

    def wrapper(*args, **kwargs):
        for i in range(3):
            print(f"  Çağrı #{i + 1}:")
            func(*args, **kwargs)

    return wrapper


@repeat_three_times
def greet(name):
    """Bir kişiyi adıyla selamla."""
    print(f"  Merhaba, {name}!")


print("\nÖrnek 2: Parametre Alan Dekoratör")
greet("Alice")

# ============================================================================
# BÖLÜM 2: PROPERTY DEKORATÖRLERİ (@property, @setter, @deleter)
# ============================================================================

print("\n" + "=" * 60)
print("BÖLÜM 2: PROPERTY DEKORATÖRLERİ")
print("=" * 60)

"""
Property Dekoratörleri Nedir?
-----------------------------
Property dekoratörleri, metotları özellik (attribute) gibi erişilebilir
şekilde tanımlamanızı sağlar. Bu şu durumlarda kullanışlıdır:

- Veri doğrulama (validation)
- Hesaplanan özellikler (computed attributes)
- Özel (private) verilere erişimi kontrol etme
"""


class Person:
    """
    Property dekoratörlerini gösteren bir sınıf.

    Property'ler, basit özellik sözdizimini kullanmaya devam ederken
    özellikleri okuma ve değiştirme sırasında doğrulama ve ek mantık
    eklememizi sağlar.
    """

    def __init__(self, name, age):
        """
        Bir Person nesnesi oluşturur.

        Args:
            name (str): Kişinin adı
            age (int): Kişinin yaşı
        """
        self.__name = name  # Özel özellik (gelenek olarak __ ile başlar)
        self.__age = age

    @property
    def name(self):
        """
        name özelliği için getter metodu.

        @property dekoratörü sayesinde _name değerine normal bir özellik gibi
        (person.name) erişebiliriz; metot çağırmamız gerekmez (person.name()).

        Returns:
            str: Kişinin adı
        """
        print("  📖 İsim alınıyor...")
        return self.__name

    @name.setter
    def name(self, value):
        """
        Doğrulama içeren name setter metodu.

        person.name = "John" şeklinde bir atama yaptığınızda çalışır.
        Burada doğrulama mantığı ekleyebiliriz.

        Args:
            value (str): Yeni isim değeri

        Raises:
            ValueError: İsim boşsa veya string değilse
        """
        print(f"  ✏️  İsim şu değere ayarlanıyor: {value}")
        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty!")
        self.__name = value

    @name.deleter
    def name(self):
        """
        name özelliği için deleter metodu.

        del person.name kullandığınızda çalışır.

        Temizleme işlemleri için kullanışlıdır.
        """
        print("  🗑️  İsim siliniyor...")
        self.__name = None

    @property
    def age(self):
        """
        age özelliği için getter metodu.

        Returns:
            int: Kişinin yaşı
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Doğrulama içeren age setter metodu.

        Args:
            value (int): Yeni yaş değeri

        Raises:
            ValueError: Yaş negatifse veya tam sayı değilse
        """
        if not isinstance(value, int):
            raise ValueError("Age must be an integer!")
        if value < 0:
            raise ValueError("Age cannot be negative!")
        if value > 150:
            raise ValueError("Age seems unrealistic!")
        self.__age = value

    @property
    def is_adult(self):
        """
        Hesaplanan bir özellik (salt okunur).

        Bu özelliğin bir setter'ı yoktur; değeri yaştan hesaplanır.
        Bu, property'lerin değerleri anlık olarak nasıl hesaplayabildiğini
        gösterir.

        Returns:
            bool: Kişi 18 yaşında veya daha büyükse True
        """
        return self.__age >= 18


# Property dekoratörlerinin kullanımı
print("\nÖrnek 3: @property Kullanımı")
person = Person("Bob", 25)
print(f"Name: {person.name}")  # Getter çağrılır
print(f"Age: {person.age}")
print(f"Is adult? {person.is_adult}")

print("\nÖrnek 4: @setter Kullanımı")
person.name = "Robert"  # Setter çağrılır
person.age = 26

print("\nÖrnek 5: Property Doğrulaması")
try:
    person.age = -5  # Bu bir hata oluşturacaktır
except ValueError as e:
    print(f"  ❌ Hata: {e}")

print("\nÖrnek 6: @deleter Kullanımı")
del person.name  # Deleter çağrılır
print(f"Silme işleminden sonraki isim: {person.name}")

# ============================================================================
# BÖLÜM 3: STATİK METOTLAR (@staticmethod)
# ============================================================================

print("\n" + "=" * 60)
print("BÖLÜM 3: STATİK METOTLAR")
print("=" * 60)

"""
@staticmethod Nedir?
--------------------
Statik metot, bir sınıfa ait olan ancak ne sınıfa ne de nesneye erişen
veya onları değiştiren bir metottur. Normal bir fonksiyon gibidir,
ancak sınıfın amacıyla ilişkili olduğu için sınıf içerisinde
organize edilmiştir.

@staticmethod şu durumlarda kullanılır:
- Metodun nesneye (self) veya sınıfa (cls) erişmesi gerekmiyorsa
- Metot, sınıfla ilişkili yardımcı (utility) bir fonksiyonsa
"""


class MathOperations:
    """Matematiksel yardımcı fonksiyonlar içeren bir sınıf."""

    @staticmethod
    def add(x, y):
        """
        İki sayıyı toplar.

        Bu bir statik metottur çünkü herhangi bir nesneye veya sınıf
        değişkenine erişmeye ihtiyaç duymaz; sadece bir hesaplama yapar.

        Args:
            x (float): Birinci sayı
            y (float): İkinci sayı

        Returns:
            float: x ve y'nin toplamı
        """
        return x + y

    @staticmethod
    def multiply(x, y):
        """
        İki sayıyı çarpar.

        Args:
            x (float): Birinci sayı
            y (float): İkinci sayı

        Returns:
            float: x ve y'nin çarpımı
        """
        return x * y

    @staticmethod
    def is_even(number):
        """
        Bir sayının çift olup olmadığını kontrol eder.

        Args:
            number (int): Kontrol edilecek sayı

        Returns:
            bool: Çift ise True, tek ise False
        """
        return number % 2 == 0


# Statik metotların kullanımı
print("\nÖrnek 7: Statik Metotlar")
print(f"5 + 3 = {MathOperations.add(5, 3)}")
print(f"5 * 3 = {MathOperations.multiply(5, 3)}")
print(f"4 çift mi? {MathOperations.is_even(4)}")
print(f"7 çift mi? {MathOperations.is_even(7)}")

# Statik metotları nesneler üzerinden de çağırabilirsiniz (ancak yaygın değildir)
math_ops = MathOperations()
print(f"Nesne üzerinden çağrı: 10 + 5 = {math_ops.add(10, 5)}")

# ============================================================================
# BÖLÜM 4: SINIF METOTLARI (@classmethod)
# ============================================================================

print("\n" + "=" * 60)
print("BÖLÜM 4: SINIF METOTLARI")
print("=" * 60)

"""
@classmethod Nedir?
-------------------
Bir sınıf metodu, ilk parametre olarak nesneyi (self) değil,
sınıfın kendisini (cls) alır. Sınıf seviyesindeki verilere erişebilir
ve bunları değiştirebilir.

@classmethod şu durumlarda kullanılır:
- Alternatif kurucular (factory methods)
- Sınıf değişkenlerine erişmesi veya onları değiştirmesi gereken metotlar
"""


class Pizza:
    """Alternatif kurucular için sınıf metotlarını gösteren bir sınıf."""

    # Sınıf değişkeni (tüm nesneler tarafından paylaşılır)
    total_pizzas_made = 0

    def __init__(self, ingredients):
        """
        Verilen malzemelerle bir Pizza oluşturur.

        Args:
            ingredients (list): Malzeme isimlerini içeren liste
        """
        self.ingredients = ingredients
        Pizza.total_pizzas_made += 1

    def __repr__(self):
        """Pizzanın metinsel gösterimi."""
        return f"Pizza({', '.join(self.ingredients)})"

    @classmethod
    def margherita(cls):
        """
        Margherita pizza oluşturmak için fabrika (factory) metodu.

        Bu, alternatif bir kurucu gibi davranan bir sınıf metodudur.
        Pizza(['tomato', 'mozzarella', 'basil']) yazmak yerine
        doğrudan Pizza.margherita() çağırabilirsiniz.

        Returns:
            Pizza: Bir Margherita pizza nesnesi
        """
        return cls(['tomato sauce', 'mozzarella', 'basil'])

    @classmethod
    def pepperoni(cls):
        """
        Pepperoni pizza oluşturmak için fabrika (factory) metodu.

        Returns:
            Pizza: Bir Pepperoni pizza nesnesi
        """
        return cls(['tomato sauce', 'mozzarella', 'pepperoni'])

    @classmethod
    def get_total_pizzas(cls):
        """
        Oluşturulan toplam pizza sayısını döndürür.

        Bu sınıf metodu, total_pizzas_made sınıf değişkenine erişir.

        Returns:
            int: Oluşturulan toplam pizza sayısı
        """
        return cls.total_pizzas_made


# Sınıf metotlarının kullanımı
print("\nÖrnek 8: Factory Metodu Olarak Sınıf Metotları")
pizza1 = Pizza.margherita()
pizza2 = Pizza.pepperoni()
pizza3 = Pizza(['BBQ sauce', 'chicken', 'onions'])

print(f"Pizza 1: {pizza1}")
print(f"Pizza 2: {pizza2}")
print(f"Pizza 3: {pizza3}")
print(f"Oluşturulan toplam pizza sayısı: {Pizza.get_total_pizzas()}")

# ============================================================================
# BÖLÜM 5: SOYUT METOTLAR (@abstractmethod)
# ============================================================================

print("\n" + "=" * 60)
print("BÖLÜM 5: SOYUT METOTLAR")
print("=" * 60)

"""
@abstractmethod Nedir?
----------------------
Soyut metot (abstract method), bir temel sınıfta tanımlanan ve
somut (soyut olmayan) alt sınıflar tarafından mutlaka uygulanması
gereken bir metottur. Bir sözleşme (contract) gibi düşünülebilir.

@abstractmethod şu durumlarda kullanılır:
- Alt sınıfların uyması gereken bir arayüz tanımlamak istediğinizde
- Temel sınıftan doğrudan nesne oluşturulmasını engellemek istediğinizde
- Belirli metotların alt sınıflarda uygulanmasını garanti etmek istediğinizde
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Hayvanlar için soyut temel sınıf.

    Bu sınıftan doğrudan nesne oluşturulamaz.
    Her alt sınıf tüm soyut metotları uygulamak zorundadır.
    """

    def __init__(self, name):
        """
        Bir hayvanı isimle başlatır.

        Args:
            name (str): Hayvanın adı
        """
        self.name = name

    @abstractmethod
    def make_sound(self):
        """
        Ses çıkarma için soyut metot.

        Her hayvan alt sınıfı bu metodu uygulamak zorundadır.
        Bu sayede tüm hayvanların ses çıkarabilmesi garanti edilir,
        ancak her hayvan kendine özgü bir ses çıkarır.
        """
        pass

    @abstractmethod
    def move(self):
        """
        Hareket için soyut metot.

        Her hayvan alt sınıfı bu metodu uygulamak zorundadır.
        """
        pass

    def sleep(self):
        """
        Somut metot (soyut değildir).

        Bu metodun bir uygulaması vardır ve alt sınıflar tarafından
        ezilmesi (override edilmesi) zorunlu değildir
        (ancak isterlerse edebilirler).
        """
        print(f"  {self.name} uyuyor... 😴")


class Dog(Animal):
    """Animal sınıfının köpekler için somut uygulaması."""

    def make_sound(self):
        """Köpekler havlar."""
        print(f"  {self.name} diyor ki: Hav! Hav! 🐕")

    def move(self):
        """Köpekler koşar."""
        print(f"  {self.name} dört ayağı üzerinde koşuyor! 🏃")


class Bird(Animal):
    """Animal sınıfının kuşlar için somut uygulaması."""

    def make_sound(self):
        """Kuşlar cıvıldar."""
        print(f"  {self.name} diyor ki: Cik cik! 🐦")

    def move(self):
        """Kuşlar uçar."""
        print(f"  {self.name} gökyüzünde uçuyor! 🦅")


# Soyut metotların kullanımı
print("\nÖrnek 9: Soyut Metotlar")
dog = Dog("Buddy")
dog.make_sound()
dog.move()
dog.sleep()

print()
bird = Bird("Tweety")
bird.make_sound()
bird.move()
bird.sleep()

print("\nÖrnek 10: Soyut Sınıftan Nesne Oluşturulamaz")
try:
    # Animal soyut bir sınıf olduğu için bu hata oluşturacaktır
    animal = Animal("Generic")
except TypeError as e:
    print(f"  ❌ Hata: {e}")

# ============================================================================
# BÖLÜM 6: FONKSİYON AŞIRI YÜKLEME (@overload)
# ============================================================================

print("\n" + "=" * 60)
print("BÖLÜM 6: FONKSİYON AŞIRI YÜKLEME")
print("=" * 60)

"""
@overload Nedir?
----------------
Python, Java veya C++ gibi geleneksel fonksiyon aşırı yüklemeyi
(function overloading) desteklemez.

@overload dekoratörü, bir fonksiyonun farklı parametre türü
kombinasyonlarını kabul edebileceğini belirtmek için tip ipuçlarında
(type hints) kullanılır.

Not: @overload yalnızca mypy gibi statik tip denetleyicileri için
tip bilgisi sağlar. Yine de gerçek bir uygulama yazmanız gerekir.
"""

from typing import overload, Union


class Calculator:
    """Tip ipuçlarıyla fonksiyon aşırı yüklemeyi gösteren hesap makinesi."""

    @overload
    def add(self, a: int, b: int) -> int:
        ...

    @overload
    def add(self, a: int, b: int, c: int) -> int:
        ...

    def add(self, a: int, b: int, c: int | None = None) -> int:
        if c is None:
            return a + b
        return a + b + c

    @overload
    def process(self, value: int) -> int:
        """Bir tam sayıyı işler."""
        ...

    @overload
    def process(self, value: str) -> str:
        """Bir metni işler."""
        ...

    def process(self, value: Union[int, str]) -> Union[int, str]:
        """
        Bir değeri işler (gerçek uygulama).

        Yukarıdaki @overload dekoratörleri yalnızca tip ipuçlarıdır.
        Her iki durumu da yöneten asıl uygulama budur.

        Args:
            value: Bir int veya str değeri

        Returns:
            Eğer int ise: value * 2 döndürür
            Eğer str ise: değeri büyük harfe çevirip döndürür
        """
        if isinstance(value, int):
            print(f"  Tam sayı işleniyor: {value}")
            return value * 2
        elif isinstance(value, str):
            print(f"  Metin işleniyor: {value}")
            return value.upper()
        else:
            raise TypeError("Value must be int or str")


# Aşırı yüklenmiş fonksiyonların kullanımı
print("\nÖrnek 11: Fonksiyon Aşırı Yükleme")
calc = Calculator()
result1 = calc.process(5)
print(f"  Sonuç: {result1}")

result2 = calc.process("hello")
print(f"  Sonuç: {result2}")

# ============================================================================
# BÖLÜM 7: FINAL SINIFLAR VE METOTLAR (@final)
# ============================================================================

print("\n" + "=" * 60)
print("BÖLÜM 7: FINAL DEKORATÖRÜ")
print("=" * 60)

"""
@final Nedir?
-------------
@final dekoratörü, bir sınıfın alt sınıfının oluşturulmaması gerektiğini
veya bir metodun ezilmemesi (override edilmemesi) gerektiğini belirtir.
Bu, mypy gibi statik tip denetleyicileri için bir tip kontrol ipucudur.

Not: Python çalışma zamanında (runtime) alt sınıf oluşturmayı veya
override işlemini engellemez, ancak tip denetleyicileri sizi uyarır.
"""

from typing import final


class BaseGame:
    """Final ve final olmayan metotlar içeren temel oyun sınıfı."""

    def start(self):
        """Oyunu başlatır - alt sınıflar tarafından override edilebilir."""
        print("  🎮 Oyun başlıyor...")

    @final
    def calculate_score(self, points: int) -> int:
        """
        Skoru hesaplar - final olarak işaretlenmiştir.

        Bu metot alt sınıflar tarafından override EDİLMEMELİDİR çünkü
        puanlama mantığının tutarlı kalması gerekir.

        Args:
            points (int): Kazanılan temel puan

        Returns:
            int: Bonus eklenmiş son skor
        """
        bonus = 100
        return points + bonus

    def end(self):
        """Oyunu bitirir - alt sınıflar tarafından override edilebilir."""
        print("  🏁 Oyun bitti!")


class MyGame(BaseGame):
    """Belirli bir oyun uygulaması."""

    def start(self):
        """start metodunu override eder (buna izin verilir)."""
        print("  🎮 MyGame özel açılış ekranıyla başlıyor!")

    # Bunun yorumunu kaldırırsanız bir tip denetleyici sizi uyarır:
    # def calculate_score(self, points: int) -> int:
    #     # ❌ Tip denetleyici uyarısı: Final metot override edilemez
    #     return points * 2


@final
class SecretAlgorithm:
    """
    Final olarak işaretlenmiş bir sınıf - alt sınıfı oluşturulmamalıdır.

    Genişletilmesini istemediğiniz sınıflarda @final kullanabilirsiniz;
    bunun nedeni güvenlik veya tutarlılık olabilir.
    """

    def process(self):
        """Gizli algoritma ile veriyi işler."""
        print("  🔒 Gizli algoritma ile işleniyor...")


# Final dekoratörünün kullanımı
print("\nÖrnek 12: Final Metotlar")
game = MyGame()
game.start()
score = game.calculate_score(50)
print(f"  Son skor: {score}")
game.end()

print("\nÖrnek 13: Final Sınıf")
secret = SecretAlgorithm()
secret.process()

# Bunun yorumunu kaldırırsanız bir tip denetleyici sizi uyarır:
# class MySecretAlgorithm(SecretAlgorithm):  # ❌ Tip denetleyici uyarısı
#     pass


# ============================================================================
# BÖLÜM 8: OVERRIDE DEKORATÖRÜ (@override)
# ============================================================================

print("\n" + "=" * 60)
print("BÖLÜM 8: OVERRIDE DEKORATÖRÜ")
print("=" * 60)

"""
@override Nedir?
----------------
@override dekoratörü (Python 3.12+ sürümlerinde bulunur), bir metodun
üst sınıftaki bir metodu ezmek (override etmek) amacıyla yazıldığını
açıkça belirtir.

Bu sayede, bir metodu override ettiğinizi düşündüğünüz halde aslında
etmediğiniz durumlar (örneğin yazım hataları veya imza uyuşmazlıkları)
tespit edilebilir.

Not: Python sürümünüz 3.12'den küçükse typing_extensions kullanabilirsiniz.
"""

try:
    from typing import override
except ImportError:
    # Python < 3.12 için typing_extensions kullanılır
    from typing_extensions import override


class Shape:
    """Şekiller için temel sınıf."""

    def area(self) -> float:
        """
        Şeklin alanını hesaplar.

        Returns:
            float: Alan değeri
        """
        return 0.0

    def perimeter(self) -> float:
        """
        Şeklin çevresini hesaplar.

        Returns:
            float: Çevre değeri
        """
        return 0.0


class Rectangle(Shape):
    """Dikdörtgen şeklinin uygulaması."""

    def __init__(self, width: float, height: float):
        """
        Bir dikdörtgen oluşturur.

        Args:
            width (float): Dikdörtgenin genişliği
            height (float): Dikdörtgenin yüksekliği
        """
        self.width = width
        self.height = height

    @override
    def area(self) -> float:
        """
        Dikdörtgenin alanını hesaplar.

        @override dekoratörü tip denetleyicilere şunu söyler:
        "Üst sınıftaki area metodunu bilerek override ediyorum."

        Eğer üst sınıfta area metodu olmasaydı, tip denetleyici
        sizi uyarırdı.

        Returns:
            float: Genişlik × yükseklik
        """
        return self.width * self.height

    @override
    def perimeter(self) -> float:
        """
        Dikdörtgenin çevresini hesaplar.

        Returns:
            float: 2 * (genişlik + yükseklik)
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Daire şeklinin uygulaması."""

    def __init__(self, radius: float):
        """
        Bir daire oluşturur.

        Args:
            radius (float): Dairenin yarıçapı
        """
        self.radius = radius

    @override
    def area(self) -> float:
        """
        Dairenin alanını hesaplar.

        Returns:
            float: π * yarıçap²
        """
        import math
        return math.pi * self.radius ** 2

    @override
    def perimeter(self) -> float:
        """
        Dairenin çevresini hesaplar.

        Returns:
            float: 2 * π * yarıçap
        """
        import math
        return 2 * math.pi * self.radius


# Override dekoratörünün kullanımı
print("\nÖrnek 14: Override Dekoratörü")
rect = Rectangle(5, 3)
print(f"Dikdörtgen (5x3):")
print(f"  Alan: {rect.area():.2f}")
print(f"  Çevre: {rect.perimeter():.2f}")

print()
circle = Circle(4)
print(f"Daire (yarıçap=4):")
print(f"  Alan: {circle.area():.2f}")
print(f"  Çevre: {circle.perimeter():.2f}")

# ============================================================================
# BONUS BÖLÜM: DEKORATÖRLERİ BİRLEŞTİRME
# ============================================================================

print("\n" + "=" * 60)
print("BONUS: BİRDEN FAZLA DEKORATÖRÜ BİRLEŞTİRME")
print("=" * 60)

"""
Aynı fonksiyon veya metod üzerinde birden fazla dekoratör kullanabilirsiniz.

Dekoratörler aşağıdan yukarıya doğru uygulanır
(yani fonksiyona en yakın olan ilk çalışır).
"""


def multiply_decorator(func):
    def wrapper(x: int):
        return func(x) * 2
    return wrapper


def other_decorator(func):
    def wrapper(x: int):
        return func(x) * 4
    return wrapper


@multiply_decorator
@other_decorator
def calculate(x: int):
    return x * 2


print(calculate(10))

# ============================================================================
# ÖZET VE EN İYİ UYGULAMALAR
# ============================================================================

print("\n" + "=" * 60)
print("ÖZET VE EN İYİ UYGULAMALAR")
print("=" * 60)

print("""
📚 Öğrendiklerimiz:

1. TEMEL DEKORATÖRLER
   - Diğer fonksiyonların davranışını değiştiren fonksiyonlar
   - Kullanım: Orijinal kodu değiştirmeden yeni özellikler eklemek

2. @property, @setter, @deleter
   - Metotlara özellik (attribute) gibi erişim sağlar
   - Kullanım: Veri doğrulama, hesaplanan özellikler

3. @staticmethod
   - Nesneye veya sınıfa erişmesi gerekmeyen metotlar
   - Kullanım: Sınıfla ilişkili yardımcı fonksiyonlar

4. @classmethod
   - İlk parametre olarak sınıfı alan metotlar
   - Kullanım: Alternatif kurucular, sınıf değişkenlerine erişim

5. @abstractmethod
   - Alt sınıflar tarafından uygulanması zorunlu metotlar
   - Kullanım: Arayüz tanımlama, uygulamayı zorunlu kılma

6. @overload
   - Birden fazla fonksiyon imzası için tip ipuçları
   - Kullanım: Daha iyi tip kontrolü ve IDE desteği

7. @final
   - Metotların override edilmesini veya sınıfların kalıtılmasını engeller
   - Kullanım: Kritik metotların değişmeden kalmasını sağlamak

8. @override
   - Override edilen metotları açıkça belirtir
   - Kullanım: Override işlemlerindeki hataları yakalamak

💡 En İyi Uygulamalar:

- Veri doğrulama ve hesaplanan değerler için @property kullanın
- Yardımcı fonksiyonlar için @staticmethod kullanın
- Alternatif kurucular için @classmethod kullanın
- Net arayüzler tanımlamak için @abstractmethod kullanın
- Niyetinizi açıkça göstermek için @override kullanın
- Dekoratörleri gereğinden fazla kullanmayın; kodun okunabilirliğini koruyun
- Dekoratörlerin amacını açıklayan net docstring'ler ekleyin

🎯 Hangi Durumda Hangisini Kullanmalı?

- Doğrulama gerekiyor mu? → @property + @setter
- Yardımcı fonksiyon gerekiyor mu? → @staticmethod
- Factory (üretici) metot gerekiyor mu? → @classmethod
- Arayüz/sözleşme gerekiyor mu? → @abstractmethod
- Tip ipuçları gerekiyor mu? → @overload
- Override işlemini engellemek gerekiyor mu? → @final
- Üst sınıftaki metodu override mı ediyorsunuz? → @override

İyi kodlamalar! 🐍✨
""")

print("\n" + "=" * 60)
print("EĞİTİMİN SONU")
print("=" * 60)