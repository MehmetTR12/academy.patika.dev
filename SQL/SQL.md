# ODEV 1

> Bu repo'da Patika.dev'in [SQL](https://academy.patika.dev/courses/sql) eğitiminde verilen ödevlerin cevapları bulunmaktadır.  
> Data = [dvdrental](https://www.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip)

### Aşağıdaki sorgu senaryolarını dvdrental örnek veri tabanı üzerinden gerçekleştiriniz.

1. film tablosunda bulunan title ve description sütunlarındaki verileri sıralayınız.

` 
SELECT title, description FROM film;
` 

2. film tablosunda bulunan tüm sütunlardaki verileri film uzunluğu (length) 60 dan büyük VE 75 ten küçük olma koşullarıyla sıralayınız.

` 
SELECT * FROM film
WHERE length > 60 AND length < 75;
` 

3. film tablosunda bulunan tüm sütunlardaki verileri rental_rate 0.99 VE replacement_cost 12.99 VEYA 28.99 olma koşullarıyla sıralayınız.

` 
SELECT * FROM film
WHERE rental_rate = 0.99 AND replacement_cost = 12.99 OR replacement_cost = 28.99 ;
` 

4. customer tablosunda bulunan first_name sütunundaki değeri 'Mary' olan müşterinin last_name sütunundaki değeri nedir?

` 
SELECT last_name FROM customer
WHERE first_name = 'Mary';
` 

5. film tablosundaki uzunluğu(length) 50 ten büyük OLMAYIP aynı zamanda rental_rate değeri 2.99 veya 4.99 OLMAYAN verileri sıralayınız.

` 
SELECT * FROM film
WHERE NOT(length > 50 AND rental_rate = 2.99 OR rental_rate = 4.99);
`

# ODEV 2

1. film tablosunda bulunan tüm sütunlardaki verileri replacement cost değeri 12.99 dan büyük eşit ve 16.99 küçük olma koşuluyla sıralayınız ( BETWEEN - AND yapısını kullanınız.)

`
SELECT * FROM film
WHERE replacement_cost BETWEEN 12.99 AND 16.99;
`

2. actor tablosunda bulunan first_name ve last_name sütunlardaki verileri first_name 'Penelope' veya 'Nick' veya 'Ed' değerleri olması koşuluyla sıralayınız. ( IN operatörünü kullanınız.)

`
SELECT first_name, last_name FROM actor
WHERE first_name IN ('Penelope', 'Nick', 'Ed');
`

3. film tablosunda bulunan tüm sütunlardaki verileri rental_rate 0.99, 2.99, 4.99 VE replacement_cost 12.99, 15.99, 28.99 olma koşullarıyla sıralayınız. ( IN operatörünü kullanınız.)

`
SELECT * FROM film
WHERE rental_rate IN (0.99, 2.99, 4.99) AND replacement_cost IN (12.99, 15.99, 28.99);
`

# ODEV 3

1. country tablosunda bulunan country sütunundaki ülke isimlerinden 'A' karakteri ile başlayıp 'a' karakteri ile sonlananları sıralayınız.

`
SELECT country FROM country
WHERE country LIKE 'A%a';
`

2. country tablosunda bulunan country sütunundaki ülke isimlerinden en az 6 karakterden oluşan ve sonu 'n' karakteri ile sonlananları sıralayınız.

`
SELECT country FROM country
WHERE country LIKE '%_____n';
`

3. film tablosunda bulunan title sütunundaki film isimlerinden en az 4 adet büyük ya da küçük harf farketmesizin 'T' karakteri içeren film isimlerini sıralayınız.

`
SELECT title FROM film
WHERE title LIKE '%t%t%t%t%';
`

4. film tablosunda bulunan tüm sütunlardaki verilerden title 'C' karakteri ile başlayan ve uzunluğu (length) 90 dan büyük olan ve rental_rate 2.99 olan verileri 
sıralayınız.

`
SELECT * FROM film
WHERE title LIKE 'C%' AND length > 90 AND rental_rate = 2.99;
`

# ODEV 4

1. film tablosunda bulunan replacement_cost sütununda bulunan birbirinden farklı değerleri sıralayınız.

`
SELECT DISTINC replacement_cost FROM film;
`
   
2. film tablosunda bulunan replacement_cost sütununda birbirinden farklı kaç tane veri vardır?

`
SELECT COUNT(replacement_cost) FROM film;
`

3. film tablosunda bulunan film isimlerinde (title) kaç tanesini T karakteri ile başlar ve aynı zamanda rating 'G' ye eşittir?

`
SELECT COUNT(title) FROM film
WHERE title LIKE 'T%' AND rating = 'G';
`

4. country tablosunda bulunan ülke isimlerinden (country) kaç tanesi 5 karakterden oluşmaktadır?

`
SELECT COUNT(country) FROM country
WHERE country LIKE '_____';
`

5. city tablosundaki şehir isimlerinin kaç tanesi 'R' veya r karakteri ile biter?

`
SELECT COUNT(city) FROM city
WHERE city LIKE '%R' OR city LIKE '%r';
`

# ODEV 5

1. film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en uzun (length) 5 filmi sıralayınız.

`
SELECT * FROM film
WHERE title LIKE '%n'
ORDER BY lenght DESC;
LIMIT 5;
`

2. film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en kısa (length) ikinci(6,7,8,9,10) 5 filmi(6,7,8,9,10) sıralayınız.

`
SELECT * FROM film
WHERE title LIKE '%n'
ORDER BY lenght ASC;
OFFSET 5
LIMIT 5;
`

3. customer tablosunda bulunan last_name sütununa göre azalan yapılan sıralamada store_id 1 olmak koşuluyla ilk 4 veriyi sıralayınız.

`
SELECT * FROM customer
WHERE store_id = 1
ORDER BY last_name DESC
LIMIT 4;
`

# ODEV 6

1. film tablosunda bulunan rental_rate sütunundaki değerlerin ortalaması nedir?

`
SELECT AVG(rental_rate) FROM film;
`

2. film tablosunda bulunan filmlerden kaç tanesi 'C' karakteri ile başlar?

`
SELECT COUNT(title) FROM film
WHERE title LIKE 'C%';
`

3. film tablosunda bulunan filmlerden rental_rate değeri 0.99 a eşit olan en uzun (length) film kaç dakikadır?

`
SELECT MAX(length) FROM film
WHERE rental_rate değeri = 0.99;
`

4. film tablosunda bulunan filmlerin uzunluğu 150 dakikadan büyük olanlarına ait kaç farklı replacement_cost değeri vardır?

`
SELECT COUNT(DISTINCT replacement_cost) FROM film
WHERE length > 150;
`

# ODEV 7

film tablosunda bulunan filmleri rating değerlerine göre gruplayınız.

`
SELECT rating, COUNT(*) FROM film
GROUP BY rating;
`

film tablosunda bulunan filmleri replacement_cost sütununa göre grupladığımızda film sayısı 50 den fazla olan replacement_cost değerini ve karşılık gelen film sayısını sıralayınız.

`
SELECT replacement_cost, COUNT(*) FROM film
GROUP BY replacement_cost HAVING COUNT(*) > 50;
`

3. customer tablosunda bulunan store_id değerlerine karşılık gelen müşteri sayılarını nelerdir?

`
SELECT store_id, COUNT(*) FROM customer
GROUP BY store_id;
`

4. city tablosunda bulunan şehir verilerini country_id sütununa göre gruplandırdıktan sonra en fazla şehir sayısı barındıran country_id bilgisini ve şehir sayısını paylaşınız.

`
SELECT country_id, COUNT(*) FROM city 
GROUP BY country_id 
ORDER BY city_count DESC 
LIMIT 1;
`

# ODEV 8


1. test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.

`
CREATE TABLE employee (
   id INTEGER,
   name VARCHAR(50),
   birthday DATE,
   email VARCHAR(100)
);
`

2. Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.

`
insert into employee (id, name, email, birthday) values (1, 'Edee', 'eshanahan0@surveymonkey.com', '1931-06-22');
insert into employee (id, name, email, birthday) values (2, 'Matthieu', 'mpurkis1@storify.com', '1909-06-21');
insert into employee (id, name, email, birthday) values (3, 'Obediah', 'othing2@aboutads.info', '1988-08-15');
insert into employee (id, name, email, birthday) values (4, 'Darn', 'dtolussi3@newyorker.com', '1996-01-06');
insert into employee (id, name, email, birthday) values (5, 'Delbert', 'dsarson4@alibaba.com', '1907-12-05');
insert into employee (id, name, email, birthday) values (6, 'Ulric', 'uphelipeau5@senate.gov', '1901-12-30');
insert into employee (id, name, email, birthday) values (7, 'Farris', 'fkobpal6@merriam-webster.com', '1962-06-09');
insert into employee (id, name, email, birthday) values (8, 'Nanci', 'nsimmance7@japanpost.jp', '1922-04-16');
insert into employee (id, name, email, birthday) values (9, 'Elmer', 'eculverhouse8@ovh.net', '1970-05-02');
insert into employee (id, name, email, birthday) values (10, 'Eolanda', 'egimenez9@oracle.com', '1944-11-29');
insert into employee (id, name, email, birthday) values (11, 'Mose', 'mberthota@senate.gov', '2002-08-03');
insert into employee (id, name, email, birthday) values (12, 'Bili', 'bhaslamb@yandex.ru', '1955-05-29');
insert into employee (id, name, email, birthday) values (13, 'Clerc', 'cduftonc@telegraph.co.uk', '1974-04-19');
insert into employee (id, name, email, birthday) values (14, 'Tessi', 'tgarteryd@eventbrite.com', '1910-12-09');
insert into employee (id, name, email, birthday) values (15, 'Catherin', 'csiggine@rambler.ru', '1947-03-08');
insert into employee (id, name, email, birthday) values (16, 'Hyman', 'hbedboroughf@naver.com', '1913-12-01');
insert into employee (id, name, email, birthday) values (17, 'Culley', 'croyansg@hexun.com', '1995-10-02');
insert into employee (id, name, email, birthday) values (18, 'Kiele', 'kaylesburyh@plala.or.jp', '1928-11-26');
insert into employee (id, name, email, birthday) values (19, 'Seamus', 'sdanbyei@unicef.org', '1917-11-27');
insert into employee (id, name, email, birthday) values (20, 'Maggi', 'mscollickj@salon.com', '1955-10-26');
insert into employee (id, name, email, birthday) values (21, 'Tasha', 'thagartk@reverbnation.com', '1957-02-11');
insert into employee (id, name, email, birthday) values (22, 'Paulo', 'pbenettinil@163.com', '1943-01-01');
insert into employee (id, name, email, birthday) values (23, 'Kacy', 'kmacdwyerm@about.com', '1981-06-19');
insert into employee (id, name, email, birthday) values (24, 'Raquel', 'rdisneyn@hexun.com', '1910-08-11');
insert into employee (id, name, email, birthday) values (25, 'Brenna', 'bdymockeo@webmd.com', '1998-06-16');
insert into employee (id, name, email, birthday) values (26, 'Lorelei', 'lproudlovep@studiopress.com', '1907-12-31');
insert into employee (id, name, email, birthday) values (27, 'Venita', 'vmossopq@who.int', '1919-04-05');
insert into employee (id, name, email, birthday) values (28, 'Obadiah', 'oarchboldr@prweb.com', '1939-04-15');
insert into employee (id, name, email, birthday) values (29, 'Emmalynne', 'ebonins@home.pl', '1944-07-06');
insert into employee (id, name, email, birthday) values (30, 'Dougy', 'ddoubledayt@nature.com', '1914-11-11');
insert into employee (id, name, email, birthday) values (31, 'Berni', 'bocarrolu@house.gov', '2002-05-29');
insert into employee (id, name, email, birthday) values (32, 'Huey', 'hknottleyv@goodreads.com', '1993-06-23');
insert into employee (id, name, email, birthday) values (33, 'Rodina', 'rfanthamw@addthis.com', '1923-01-26');
insert into employee (id, name, email, birthday) values (34, 'Brad', 'blentschx@joomla.org', '1939-03-23');
insert into employee (id, name, email, birthday) values (35, 'Tybie', 'teasterbyy@alibaba.com', '1948-10-07');
insert into employee (id, name, email, birthday) values (36, 'Annetta', 'acamplinz@bbc.co.uk', '1935-07-19');
insert into employee (id, name, email, birthday) values (37, 'Dell', 'dgibard10@mlb.com', '1906-11-18');
insert into employee (id, name, email, birthday) values (38, 'Kamillah', 'kwitheford11@bizjournals.com', '1907-05-29');
insert into employee (id, name, email, birthday) values (39, 'Ryann', 'ragate12@altervista.org', '1937-08-16');
insert into employee (id, name, email, birthday) values (40, 'Kerby', 'kroskam13@cbc.ca', '1959-06-03');
insert into employee (id, name, email, birthday) values (41, 'Ethyl', 'edrinkwater14@is.gd', '1971-04-17');
insert into employee (id, name, email, birthday) values (42, 'Bartholomeus', 'bwhatling15@csmonitor.com', '1925-05-24');
insert into employee (id, name, email, birthday) values (43, 'Ari', 'aconichie16@chronoengine.com', '1909-05-22');
insert into employee (id, name, email, birthday) values (44, 'Donny', 'dpawlyn17@surveymonkey.com', '1926-06-22');
insert into employee (id, name, email, birthday) values (45, 'Orton', 'odrewe18@example.com', '1928-02-20');
insert into employee (id, name, email, birthday) values (46, 'Bonny', 'btomczykowski19@desdev.cn', '1991-09-09');
insert into employee (id, name, email, birthday) values (47, 'Larina', 'lfryers1a@springer.com', '1915-10-06');
insert into employee (id, name, email, birthday) values (48, 'Thorsten', 'tbravery1b@booking.com', '1910-05-07');
insert into employee (id, name, email, birthday) values (49, 'Alexina', 'amingame1c@unesco.org', '1901-06-24');
insert into employee (id, name, email, birthday) values (50, 'Normie', 'nmaffetti1d@reference.com', '1933-10-21');
`

3. Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.

`
UPDATE employee
SET name = 'Mehmet',
   email = 'memo@abc.com',
  birthday = '2001-07-23'
WHERE id = '19';
`
`
UPDATE employee
SET name = 'Yusuf',
    email = 'yusuf@abc.com',
    birthday = '1998-03-20'
WHERE name = 'Brad';
`
`
UPDATE employee
SET name = 'Ahmet',
    email = 'ahmet@abc.com',
    birthday = '1996-11-21'
WHERE email = 'kaylesburyh@plala.or.jp';
`
`
UPDATE employee
SET name = 'Mustafa',
    email = 'mustafa@abc.com',
    birthday = '2002-10-14'
WHERE birthday = '1935-07-19';
`
`
UPDATE employee
SET name = 'XXX',
    email = 'xxx@yyy.com',
    birthday = '2002-02-22'
WHERE name ILIKE 'D%' AND name ILIKE '%Y';
`

4. Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.

`
DELETE FROM employee
WHERE id = 47;
`
`
DELETE FROM employee
WHERE name = 'Culley';
`
`
DELETE FROM employee
WHERE email = 'egimenez9@oracle.com';
`
`
DELETE FROM employee
WHERE birthday = '1995-10-02';
`
`
DELETE FROM employee
WHERE name ILIKE 'R%' AND name ILIKE '%l';;
`



