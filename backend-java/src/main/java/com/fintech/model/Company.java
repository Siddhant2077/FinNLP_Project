package com.fintech.model;

public class Company {

    private String symbol;
    private String name;
    private String sector;

    public Company(String symbol, String name, String sector) {
        this.symbol = symbol;
        this.name = name;
        this.sector = sector;
    }

    public String getSymbol() {
        return symbol;
    }

    public String getName() {
        return name;
    }

    public String getSector() {
        return sector;
    }
}