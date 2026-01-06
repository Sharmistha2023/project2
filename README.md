## References:
          https://github.com/aravind-selvam/forest-fire-prediction
##
For pipeline : 
##
          https://github.com/oneconvergence/dkube-examples/blob/sklearn/titanic/pipeline.ipynb
##
## Curl:
##
        curl -k --location --request POST "https://18.191.162.154:32222/dkube/inference/ocdkube1/340103edac:predict" --header "Authorization: Bearer  eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0YmNkZjBmZWJmNDRiOGRhZGQxZWIyOGM2MjhkYWYxIn0.eyJ1c2VybmFtZSI6Im9jZGt1YmUxIiwicm9sZSI6ImRhdGFzY2llbnRpc3QsbWxlLHBlIiwiZGVwbG95Ijp0cnVlLCJleHAiOjUwMDAzNDI4NDUsImlhdCI6MTc2MDM0Mjg0NSwiaXNzIjoiRGt1YmUifQ.3gZK-Hz_l_tz_Fm0SfJXWyiPGhvUm1CbI5Zz13c9qR_Vwmy23sbjs5GwPXLdg041Rd44Rk0fvguXY8tZPVXSKA1KJhJ8hWNfRKgvHb4rP_KKPPKQ1fgQLhoSt0cregnrt49hlQ2F8Wxy6N4GekpCAgTFJ_PCwYmkBiNmDPNiLCNhI2n0n3N76-UAU47s5Q0YsC9zjq3oisBi8VZ7wtLMcIc-1B_VkqxrTDQl89xXGTduq1GEyr_ICqvRBd4JwTFy5k0j-rHzic4O6-ytNzb13ALSB0KIzLqw7H3rHiMr58P1Nha7SV-e2UAahPeQTtKlHpa5QMN-v_EAGA5UqKtyWg" --header "Content-Type: application/json" --data-raw '{
  "instances": [
    [29, 57, 18, 0.0, 65.7, 3.4, 7.6, 1.3, 3.4, 0, 1]
  ]
}'

##
