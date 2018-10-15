//
//  Settings.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/22/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class Setting: NSObject {
    let name: String
    let imageName: String
    
    init(name: String, imageName: String) {
        self.name = name
        self.imageName = imageName
    }
}
