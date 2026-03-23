package com.fintech.service;

import com.fintech.model.Company;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

@Service
public class PythonServiceCaller {

    private final String PYTHON_URL = "http://localhost:5000/sentiment";

    public String callPythonService(Company company) {

        RestTemplate restTemplate = new RestTemplate();

        String url = UriComponentsBuilder
                .fromUriString(PYTHON_URL)
                .queryParam("company", company.getName())
                .queryParam("symbol", company.getSymbol())
                .queryParam("sector", company.getSector())
                .toUriString();

        return restTemplate.getForObject(url, String.class);
    }
public String compareCompanies(Company c1, Company c2) {

    RestTemplate restTemplate = new RestTemplate();

    String url = UriComponentsBuilder
            .fromUriString("http://localhost:5000/compare")
            .queryParam("company1", c1.getName())
            .queryParam("symbol1", c1.getSymbol())
            .queryParam("sector1", c1.getSector())
            .queryParam("company2", c2.getName())
            .queryParam("symbol2", c2.getSymbol())
            .queryParam("sector2", c2.getSector())
            .toUriString();

    return restTemplate.getForObject(url, String.class);
}
}