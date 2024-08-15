# Kurt Geiger DevOps test

## Pre-requisites

You should have a suitable working environment, which includes a computer with Internet connection where you can write scripts on. 

You may use the Internet to search for ideas etc., as you would with any normal task at work, but we want to see what you can do on your own so getting someone to help you out is forbidden.

## CloudFormation

KGDevOpsInterview.json is a CloudFormation template that will spin up an EC2 instance. Tasks:

1) Fix the errors in the template;
2) Tag the EC2 instance with the key `Name`, and the value your first and last name;
3) Modify the stack so that `yum -y update` is executed when the instance comes up;
4) Output the EC2 instance ID;
5) Create an ALB (application load balancer), and put the instance behind it.

#### Bonus points:

6) Create an SQS queue in CloudFormation in a different stack;
7) Using CloudFormation, modify the EC2 instance template in order to allow the following command to be executed from the EC2 instance:

```sh
aws sqs get-queue-url --queue-name name-of-the-created-queue
```

## Chef

`test.rb` is a simple Chef recipe that installs Apache and writes 'Hello world' in /etc/motd. To help you rehearse the recipe, install [`chef-solo`](https://docs.chef.io/chef_install_script/) on a Linux virtual machine. Tasks:

1) Fix the syntax/errors in the recipe;
2) Set `httpd` to be enabled at boot time;
3) Create a *nix username called your firstname.lastname using the `user` Chef resource.

#### Bonus points

4) Create a cronjob that executes a test command that runs every day at 05:45 AM;
5) Set the timezone to Europe/London.

## Scripting

In the scripting language of your choice (i.e. Python, Ruby, Perl, Bash), write some code to query the Brewdog API and return some information to the user. Tasks:

1) Connect to the API at [`https://api.punkapi.com/v2/beers`](https://api.punkapi.com/v2/beers), get the results and print them out. This API is also mirrored at [`https://s3-eu-west-1.amazonaws.com/kg-it/devopsTest/api-punkapi-com-v2-beers.json`](https://s3-eu-west-1.amazonaws.com/kg-it/devopsTest/api-punkapi-com-v2-beers.json) in case the above is not working;
2) Modify your script to just print out the beer name (the name field) and the ABV field for each beer, separated by a comma (CSV format). You may find using a JSON parser useful at this point.

The start of the output should look something like the below, yours may differ slightly, that's OK:

```sh
Buzz,4.5
Pilsen Lager,6.3
Electric India,5.2
```

#### Bonus points

3) Modify your script to only return beers with an ABV greater than a specified value. This value can be hardcoded in your script, or for even more bonus points it can be a parameter chosen by the user of the script, i.e. `./getBeersGreaterThan 6`;
4) Modify your script to sort the beers by the ABV field. The decision to sort in ascending or descending order is up to you.
