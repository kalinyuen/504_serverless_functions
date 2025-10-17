# Cloud Serverless Functions

## Zoom Recording
Recording: https://drive.google.com/file/d/12htdwl6U5OQXCwx2Wq6YbHxEtIGLiUPp/view?usp=sharing

## Cloud environments
Cloud environment used and their regions: 
- Google Cloud Platform: US-central-1
- Azure: East US

## Steps to deployment
GCP: 
1. Search Cloud Run function 
2. Create new function
3. Name the function, select region and finish configuration
4. Edit main source code
5. Test and deploy.

Azure: 
1. Search Function 
2. Create new function app
3. Name the function app, select region and finish configuration
4. Create new function with HTTP trigger and set authorization level to "Function" or "Anonymous"
5. Edit main source code.
6. Test and deploy.

## Functionality showcase
GCP:
![GCP function](/GCP/gcp_req.png)
![GCP function](/GCP/gcp_test.png)

Azure:
![azure functionality](/Azure/azure_req.png)
![azure functionality](/Azure/azure_test.png)


## Public Endpoint URLs
GCP: https://lpl-cholesterol-250516108637.us-central1.run.app

Azure: https://kalin-serverless-504-gwf9avgsepezcrdb.eastus-01.azurewebsites.net/api/http_trigger1?code=xoWH1DUU4msicUZwDcFTCEohvui4LtJymXJvZyZIiIVcAzFubct9QQ==

## LDL Source Link:
https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/lipid-panel

## Example Requests
### Testing Optimal LPL level (GCP) 
```python
import requests

url = 'https://lpl-cholesterol-250516108637.us-central1.run.app'

body = {
    "lpl": 80
}

response = requests.post(url, json=body)

print(response.text)
```
Output:

```json
{"lpl intake": 80.0, "status": "optimal", "category": "Optimal (<100 mg/dL)"}
```

### Testing High LPL level (Azure)
```python
import requests

url = 'https://kalin-serverless-504-gwf9avgsepezcrdb.eastus-01.azurewebsites.net/api/http_trigger1?code=xoWH1DUU4msicUZwDcFTCEohvui4LtJymXJvZyZIiIVcAzFubct9QQ=='

body = {
    "lpl": 180
}

response = requests.post(url, json=body)

print(response.text)
```
Output:
```json
{"lpl intake": 180.0, "status": "high", "category": "High (>=160 mg/dL)"}
```

### Testing Borderline High LPL level (Azure)
```python
import requests

url = 'https://kalin-serverless-504-gwf9avgsepezcrdb.eastus-01.azurewebsites.net/api/http_trigger1?code=xoWH1DUU4msicUZwDcFTCEohvui4LtJymXJvZyZIiIVcAzFubct9QQ=='

body = {
    "lpl": 130
}

response = requests.post(url, json=body)

print(response.text)
```
Output:
```json
{"lpl intake": 130.0, "status": "borderline high", "category": "Borderline High (100-160 mg/dL)"}
```

## Comparison between GCP and Azure for serverless functions
Azure:
- Supports a wider range of triggers (HTTP, timer, blob, queue, event grid, and more), allowing for greater integration with different Azure services.
- Offers flexible authentication options, including function keys, anonymous access, and Azure Active Directory integration for secure access control.
- Provides a powerful local development environment through Visual Studio Code and Azure Functions Core Tools, enabling efficient testing and debugging before deployment.

GCP:
- Features a simple and intuitive console that makes creating and managing Cloud Functions straightforward.
- Allows fast updates and redeployment directly from the Cloud Console, minimizing setup time and speeding up development.
- Includes built-in observability tools like Cloud Logging and Cloud Trace for detailed performance monitoring and error analysis.


### Overall assessment
Both Azure and GCP deliver strong performance for running serverless workloads. Azure stands out for its flexibility, deep configuration options, and enterprise-level integrations, while GCP emphasizes simplicity, rapid setup, and ease of management. The best choice depends on user priorities where Azure is better for advanced customization and integration, and GCP for streamlined development and speed.
