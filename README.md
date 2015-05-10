GitHubProjectParser
===================================


About GitHubProjectParser
--------------

GitHubProjectParser is made for data analysts to get the statistics information of one open source project in Github.

It works more like a spider. It downloads and parses the related html pages in Github.com. It is written by Python. 

GitHubProjectParser now can only get the statistics of the members of one open source project. In the near future, it will be able to do some analytics in the data of commits.

How to use
--------------

The python script need only one parameter – the url of the main page of the project to be parsed.

The format of the command line is as follows:
python github.py url_of_project

for example, if you want to analyze the Kubernetes project, you can run the command:
python github.py https://github.com/GoogleCloudPlatform/kubernetes

It will export the result to a csv file named result.csv in the local path.

How to contribute
--------------

Just feel free to add any interesting features.