//
//  Business.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/22/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class Business: NSObject {
    
    var businessName: String  // String? means optional string
    var details: String
    var location: String
    var phone: String
    var logo: String
    var website: String
    var hours: String
    var prices: String
    

    init(name: String, details: String, location: String, phone: String, logo: String, website: String, hours: String, prices: String) {
        self.businessName = name
        self.details = details
        self.location = location
        self.phone = phone
        self.logo = logo
        self.website = website
        self.hours = hours
        self.prices = "Avg: \(prices)"
    }
    
}
