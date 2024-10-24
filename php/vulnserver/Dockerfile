FROM php:7.4-apache

# Install necessary PHP extensions and dependencies

# Install necessary PHP extensions and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    libxml2-dev \
    tcl-expect-dev \
    && docker-php-ext-install xml

# Update pear and pecl channels and install the "expect" extension
RUN pear channel-update pear.php.net \
    && pecl channel-update pecl.php.net \
    && pecl install expect

# Enable the expect extension
RUN echo "extension=expect.so" > /usr/local/etc/php/conf.d/expect.ini

# Set PHP configuration options
RUN echo "short_open_tag=Off" > /usr/local/etc/php/conf.d/short_open_tag.ini

# Change Apache to listen on port 9000
RUN sed -i 's/Listen 80/Listen 9000/' /etc/apache2/ports.conf
RUN sed -i 's/:80/:9000/g' /etc/apache2/sites-available/000-default.conf

# Copy the PHP application files to the Apache server's root directory
WORKDIR /var/www/html
COPY ./src/ .
COPY ./flag.php /etc/.flag.php

# To demonstrate SSRF AWS, comment the following out if not required.
RUN apt-get update && apt-get install -y iptables
RUN apt-get install -y iputils-ping
COPY ./setup-aws-simulator.sh /
RUN chmod +x /setup-aws-simulator.sh

# set www-data as the owner
RUN chown -R "www-data:www-data" /var/www/html && chmod -R 755 /var/www/html

# Set up entrypoint
ENTRYPOINT /setup-aws-simulator.sh && apache2-foreground
