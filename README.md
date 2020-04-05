Scrapper for downloading country wise data present in charts at https://www.worldometers.info/coronavirus/country/us/, 

![](./imgs/total_cases.png)

# Configuration

The code has been tested on windows 10. This makes use of chrome web driver. Make sure you download the web driver from here https://chromedriver.chromium.org/downloads.

Once that is done, make sure to update the ```config.py``` file. You will need to update the ```web_driver_path``` to the path of the downloaded chrome web-driver's executables.



# Execute

Once the configuration is done download the data by

```
cd <repo path>
## Download data for all countries listed at worldo-meter
python engine.py --country All --update Yes
## Download data for some countries (See country.json for valid country names)
python engine.py --country USA,Spain,Turkey --update Yes
```

The data will automatically get downloaded in the ```data``` folder

# Arguments

You can use two command line arguments,

1.  ```--country``` , it can either be ```All``` or ```USA, Spain,Italy``` for valid country names see ```country.json``` 
2. ```--update``` , should ```country.json``` be updated from worldo-meter website. Values can be ```Yes``` or ```No```

# Requirements

```
python=3.7
bs4==0.0.1
selenium==3.141.0
tqdm==4.36.1
xlrd==1.2.0
XlsxWriter==1.2.8
pandas==0.25.2
numpy==1.16.5
```

# Download pre-fetched data

I will try to upload data daily . Latest dump is here https://datasetsgun.s3.amazonaws.com/data/data_05_04_20+18_14_35.zip



# Citation

Cite this project

```
@misc{Gunnvant2020,
  author = {Gunnvant, Saini},
  title = {Worldometer_Chart_Scrapper},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
}
```

