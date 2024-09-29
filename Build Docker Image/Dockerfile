FROM shohamd/cacheflushsimulator:latest

# Set non-interactive frontend to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Remove bind9 if it exists
RUN apt-get update && apt-get remove --purge -y bind9 && apt-get autoremove -y

# Install necessary packages
RUN apt-get install -y --no-install-recommends \
    apt-utils \
    wget \
    gnupg2 \
    lsb-release \
    nsd \
    gnutls-bin \
    libgnutls28-dev

# Install Knot Resolver
RUN wget https://secure.nic.cz/files/knot-resolver/knot-resolver-release.deb && \
    dpkg -i knot-resolver-release.deb && \
    apt update && \
    apt install -y knot-resolver

# Configure Knot Resolver
RUN mkdir -p /etc/knot-resolver
COPY kresd.conf /etc/knot-resolver/kresd.conf


WORKDIR /env
