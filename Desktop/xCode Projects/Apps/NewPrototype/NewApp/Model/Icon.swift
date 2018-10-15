//
//  Video.swift
//  NewApp
//
//  Created by Jeffery Ho on 7/17/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class Icon: NSObject {
    
    var thumbnailImageName: String?  // String? means optional string
    var thumbnail: String?

    init(name: String, imageName: String) {
        self.thumbnailImageName = name
        self.thumbnail = imageName
    }
    
}

