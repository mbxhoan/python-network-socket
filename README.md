# Python Network Socket Server and API Integration with BarTender

This repository demonstrates how to create a Python network socket server and API that integrates with BarTender for label printing. The network socket integration allows you to send print jobs to BarTender using custom data.

## Prerequisites

- Python 3.x
- BarTender 2022 or later
- Integration Builder (part of BarTender)

## Setup

1. **Network Socket Server:**
   - Create a Python script that listens on a specific port for incoming print job data.
   - Parse the data and format it according to your label template in BarTender.
   - Use the BarTender REST API to send the formatted data to BarTender.

2. **Integration Builder Configuration:**
   - In BarTender, create an Integration Builder project.
   - Add a new integration using the "Network Socket" option.
   - Configure the integration to listen on the same port as your Python network socket server.
   - Map the received data fields to the appropriate BarTender variables.

3. **API Endpoint:**
   - Create a Python API (using a framework like Flask or FastAPI) that exposes an endpoint for receiving print job data.
   - When data is received, forward it to your network socket server or directly to the BarTender Integration Builder.

4. **Testing:**
   - Test the integration by sending sample data to your API endpoint.
   - Verify that BarTender processes the print job correctly.

## Usage

1. Start your Python network socket server.
2. Send print job data to the server using your API endpoint.
3. BarTender will process the data and print the labels.

Remember to replace placeholders with actual code and configuration specific to your environment. For detailed examples and step-by-step instructions, refer to the BarTender Integration Builder documentation.
