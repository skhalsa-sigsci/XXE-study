FROM tomcat:jdk8-openjdk
COPY ./ROOT /usr/local/tomcat/webapps/ROOT
COPY ./temp /usr/local/tomcat/temp

# To demonstrate SSRF AWS, comment the following out if not required.
RUN apt-get update 
RUN apt-get install -y iputils-ping iptables
COPY ./setup-aws-simulator.sh /
RUN chmod +x /setup-aws-simulator.sh

# Update Tomcat's server.xml to use port 9002
RUN sed -i 's/port="8080"/port="9002"/' /usr/local/tomcat/conf/server.xml

ENTRYPOINT /setup-aws-simulator.sh && catalina.sh run

