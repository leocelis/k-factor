# K-factor

Calculate the **organic growth rate** of your Ad.

A k-factor of 1 is in a "steady" state of neither growth nor decline, while a k-factor greater than 1 indicates exponential growth and a k-factor of less than 1 indicates an exponential decline.

Installation
-----
virtualenv -p python3 venv<br />
python3 -v venv<br />

Usage
-----
Update the following values in calc.py:

- users = total paid clicks
- shares_sent = total shares
- conversions = total conversions

**Run the script:**

`>python3 calc.py` 

**Example output:**

Total users (paid clicks): 1250<br />
Total shares generated: 2500<br />
Avg. shares per user: 2.0<br />
Total referred conversions: 1500<br />
Referred conversion rate: 60%<br />
K-factor: 1.2<br />
<br />
Your ad is working! :)<br />
<br />

**Learn more:** http://blog.leocelis.com/2018/06/16/cpa-vs-k-factor/
