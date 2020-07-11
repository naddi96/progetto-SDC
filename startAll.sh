cd login-manager
./dowloadLoginContainer.sh
docker stop loginser
docker rm loginser
docker run -d --name=loginser --network=host loginserver
cd ..
cd web-server
./dowloadServerContainer.sh
docker stop regioniser
docker rm regioniser
docker run -d --name=regioniser --network=host regioniserver
cd ..

cd mysql
docker stop mysql-va
docker run --name=mysql-va --network=host -e MYSQL_ROOT_PASSWORD=root -d mysql:5.6
docker start mysql-va
docker cp ./comandForDb.sql mysql-va:/comandForDb.sql
docker exec mysql-va /bin/sh -c 'mysql -u root -proot </comandForDb.sql'
cd ..
cd validation-authority
docker stop validation
docker rm validation
./startVa.sh