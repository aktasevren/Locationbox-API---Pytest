## Pytest ile Locationbox API Test Otomasyonu

#### Locationbox Otomasyon Projesi Genel Bilgiler

- Bu proje ile tek bir komut ile 4 farklı ortamda Locationbox testleri yapılabilmektedir.

  o Oracle Development

  o Oracle Production

  o Postgre Development

  o Postgre Production

- Yaklaşık 100 servis için kontroller yapılmaktadır.

- Her servis için hem JSON Response hem XML response kontrol edilmektedir.

- Kontroller genel olarak bir request atıldıktan sonra dönen response göre yapılmaktadır.

          assert response["response"]["status"] == "0"
          assert response["response"]["request_limit"] > "0"
          assert response["response"]["errno"] == None

- DB tarafında güncelleme yapan servisler için ( örnek SetPoiAttribute ) DB kontrolleride yapılmaktadır.

  `pytest --html=report.html --self-contained-html --capture=tee-sys -p no:warnings`

- Test sonrasında servisler için success/fail, request url, response, duration vb. sonuçlar üreten bir çıktı ( report.html ) oluşmaktadır.

![report.html](image.png)

#### Pytest Hakkında Genel Bilgiler

_Pytest_: Python tabanlı, açık kaynaklı, birim testi, fonksiyonel test ve API testi yapılabilen bir test aracıdır.
_Pytest paketinin yüklenmesi_: Python paket yükleyici (PIP) ile aşağıdaki komutu kullanarak paketi yükleyebilirsiniz.

```
pip install pytest
```

_Pytest syntax_:

1- Testleri içeren dosyaların isimleri test\_ ile başlamalı ya da \_test ile bitmelidir.

Örnek: test_locationbox.py, locationbox_test.py

2- Testleri içeren fonksiyonlar test ile başlamalıdır.

Örnek:test_get_version()
Örnek Proje
Örnek Klasör Yapısı

- demo_klasör /

  o test_demo.py

  test_demo.py için basit bir test fonksiyonu

  ```
  import pytest
  def test_file_example():
  input_value = 5
  assert input_value*5 == 25
  ```

Testlerin çalıştırılması

- pytest test_example.py => komutu ile test_demo dosyasında bulunan bütün testler çalıştırılır.
  test_example.py .F
  . başarılı testler
  F başarısız testler

- pytest test_example.py -v => komutu ile test_demo dosyasında bulunan bütün testler daha ayrıntılı (verbosity) çalıştırılır.
  test_1.py::test_example1 PASSED
  test_1.py::test_example2 FAILED

- pytest <filename> => komutu ile belirli bir test dosyası çalıştırılır.

Test Fonksiyonları
1- Test fonksiyonları belirli kelimelerle gruplanabilir.
@pytest.mark.address

    def test_file_example():
    		input_value = 5
    		assert input_value*5 == 25

- pytest -m address => komutu ile test_demo dosyasında bulunan address marklı bütün fonksiyonlar çalıştırılır.

- pytest -k example => komutu ile test_demo dosyasında bulunan example ismini içeren fonksiyonlar çalıştırılır.

2- Belirli koşullara göre test fonksiyonları atlanabilir.

- @pytest.mark.skipif(( env == "Postgre" ), reason= "Postgre method not supported" )

3- xFail ile zaten başarısız olacak testler belirlenebilir.

- @pytest.mark.xfail ( reason = = "Postgre method not supported" )




----------------------




## Pytest

- Pytest is a testing framework based on python
- It is mainly used to write API test

- **installation**\
    -pip install pytest
- *test_something.py or something_test.py* ==> Pytest automatically identifies those 
files as a test files\
                - test_example.py - valid\
                - example_test.py - valid\
                - testexample.py -invalid\
                - exampletest.py -invalid\
- Pytest requires the test function names to start with test
    - def test_file_example1(): - valid
    -    def testfile_example(): - valid
    -   def file1_method1(): - invalid
- run the test using the ```pytest```
    * test_square.py .F
        - . for successfull 
        - F for FAILED
- run the test using the ```pytest -v```
    * -v increases the verbosity.
    * test_1.py::test_sqrt PASSED \
      test_1.py::testsquare FAILED
-  Pytest command will execute all the files of format test_* or *_test in the current directory and subdirectories.
- To execute the tests from a specific file ```pytest <filename> -v```
- run the test using the ```pytest test_2.py -v```
    * test_2.py::test_greater FAILED\
    test_2.py::test_greater_equal PASSED\
    test_2.py::test_less PASSED
- To execute the tests containing a string in its name ```pytest -k <substring> -v```
- run the test using the ```pytest -k great -v```
    * test_2.py::test_greater FAILED\
      test_2.py::test_greater_equal PASSED
- Pytest allows us to use markers on test functions.
    * @pytest.mark.markername
- To run the marked tests
    * pytest -m <markername> -v
- run the test using the ```pytest -m filetwo```
    -    pytest -m engine → we run only the tests marked as engine.
    - pytest -m “body and engine” → run tests with marks both body and engine
    - pytest -m “body or engine” → run tests with mark engine or body
    - pytest -m “not entertainment” → run tests except entertainment
    - pytest -m “not ui” → doesn’t run tests with mark ui
    - pytest -m “backend not ui” → run tests with mark backend but does not run with mark ui
    * collected 5 items / 3 deselected / 2 selected\
        test_2.py::test_greater FAILED\
        test_2.py::test_less PASSED
- Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. 
    * @pytest.fixture
- We can define the fixture functions in this file to make them accessible across multiple test files.
- run the using the ```pytest test_without_fixture.py -v```
    * test_without_fixture.py::test_divisible_by_3 PASSED
    test_without_fixture.py::test_divisible_by_6 FAILED 
- Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker ```@pytest.mark.parametrize```
- run the test using the ```pytest test_parametrize.py -v```
- Skip test — A test will not be run if it is marked as skipped. ```@pytest.mark.xfail```
- Xfailed test — They will be executed, but it will not be included in the calculation of passed or failed tests. ```@pytest.mark.skip```
- **xfail reason example**
    ```
    @pytest.mark.xfail(reason="results do not match for this example")
    def test_get_a_single_cart():
        url = 'https://dummyjson.com/products/1'
        request = requests.get(url)
        response = request.json()

        product_title = response["title"]

        assert product_title == "IPhone 9"
    ```
- **skip reason example**
    ```
    platform = 'windows'
    @pytest.mark.skipif(platform == "windows",reason="does not run on windows")
    def test_skip_function():
        print("skip_function")
    ```
- run the test using the ```pytest test_skip_fail.py -v```
    * test_skip_fail.py::test_greater xfail\
        test_skip_fail.py::test_greater_equal XPASS\
        test_skip_fail.py::test_less SKIPPED
- The syntax to stop the execution of test suite soon after n number of test fails is as follows ```pytest --maxfail = <num>```
- run the using the ```pytest test_failure.py -v --maxfail 1```
- By default, pytest runs tests in sequential order. In a real scenario, a test suite will have a number of test files and each file will have a bunch of tests. This will lead to a large execution time. To overcome this, pytest provides us with an option to run tests in parallel
    ```
    pip install pytest-xdist
    ```
- run the test using the ```pytest -n 3```
    * -n <num> runs the tests by using multiple workers, here it is 3.