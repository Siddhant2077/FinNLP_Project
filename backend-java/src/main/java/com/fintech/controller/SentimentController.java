package com.fintech.controller;

import com.fintech.model.Company;
import com.fintech.service.CompanyService;
import com.fintech.service.PythonServiceCaller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class SentimentController {

    @Autowired
    private CompanyService companyService;

    @Autowired
    private PythonServiceCaller pythonServiceCaller;

@GetMapping("/compare")
public ResponseEntity<?> compare(
        @RequestParam String symbol1,
        @RequestParam String symbol2) {

    Company c1 = companyService.getCompany(symbol1);
    Company c2 = companyService.getCompany(symbol2);

    if (c1 == null || c2 == null) {
        return ResponseEntity.badRequest()
                .body("Invalid company symbol provided.");
    }

    String result = pythonServiceCaller.compareCompanies(c1, c2);

    return ResponseEntity.ok(result);
}

    @GetMapping("/sentiment")
    public ResponseEntity<?> analyze(@RequestParam String symbol) {

        Company company = companyService.getCompany(symbol);

        if (company == null) {
            return ResponseEntity.badRequest().body("Company not found");
        }

        String result = pythonServiceCaller.callPythonService(company);
        return ResponseEntity.ok(result);
    }
}