FROM ros:crystal

# Set up workspace
RUN apt update && apt install -y \
    python3-pip \
    python3-colcon-common-extensions \
    python3-pyqt5 \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install ultralytics opencv-python PyYAML

# Copy and build package
WORKDIR /workspace
COPY . /workspace
RUN . /opt/ros/crystal/setup.sh && \
    colcon build

CMD ["bash"]