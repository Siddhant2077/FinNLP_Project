package com.fintech.service;

import com.fintech.model.Company;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

import jakarta.annotation.PostConstruct;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;

@Service
public class CompanyService {

    private Map<String, Company> companyMap = new HashMap<>();

    @PostConstruct
public void loadCompanies() {
    try {
        ClassPathResource resource = new ClassPathResource("companies.csv");

        InputStream inputStream = resource.getInputStream();

        BufferedReader reader = new BufferedReader(
                new InputStreamReader(inputStream, StandardCharsets.UTF_8)
        );

        String line;
        reader.readLine(); // skip header

        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(",");

            if (parts.length >= 3) {
                String symbol = parts[0].trim();
                String name = parts[1].trim();
                String sector = parts[2].trim();

                companyMap.put(symbol, new Company(symbol, name, sector));
            }
        }

        System.out.println("Loaded companies: " + companyMap.size());

    } catch (Exception e) {
        System.out.println("Error loading company CSV");
        e.printStackTrace();
    }
}
    public Company getCompany(String symbol) {
        return companyMap.get(symbol);
    }

    public List<Company> getAllCompanies() {
        return new ArrayList<>(companyMap.values());
    }
}