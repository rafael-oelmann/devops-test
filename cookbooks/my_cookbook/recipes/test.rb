package 'httpd' do
  action :install
end

service 'httpd' do
  action [:enable, :start]
end

file '/etc/motd' do
  owner 'root'
  group 'wheel'
  mode '0644'
  content 'Hello world'
end

user 'rafael.perez' do
  action :create
end

cron 'daily_test_command' do
  minute '45'
  hour '5'
  command 'echo "Test command executed"'
  action :create
end

timezone 'Europe/London' do
  action :set
end