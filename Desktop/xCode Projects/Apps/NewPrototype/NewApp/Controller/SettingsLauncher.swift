//
//  SettingsLauncher.swift
//  NewPrototype
//
//  Created by Jeffery Ho on 7/19/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class SettingsLauncher: NSObject, UICollectionViewDataSource, UICollectionViewDelegate, UICollectionViewDelegateFlowLayout {
    
// Constants
//==============================================================================================================================================================================================================================================
    let blackView = UIView()
    
    let collectionView: UICollectionView = {
        let layout = UICollectionViewFlowLayout()
        let cv = UICollectionView(frame: .zero, collectionViewLayout: layout)
        cv.backgroundColor = UIColor.white
        return cv
    }()
    
    let cellId = "cellID"
    let cellHeight: CGFloat = 50
    
    let settings: [Setting] = {
        return [Setting(name: "Settings", imageName: "settings"), Setting(name: "Terms & Privacy Policy", imageName: "privacy"), Setting(name: "Send Feedback", imageName: "feedback"), Setting(name: "Help", imageName: "help"), Setting(name: "Account", imageName: "account"), Setting(name: "Cancel", imageName: "cancel")]
    }()
    
    
// Variables
//==============================================================================================================================================================================================================================================
    var homeController: HomeController?
    
    
// Body
//==============================================================================================================================================================================================================================================
    // This function is called when the more button is pressed
    @objc func showSettings() {
        //Show menu
        
        if let window = UIApplication.shared.keyWindow {
            blackView.backgroundColor = UIColor(white: 0, alpha: 0.5)
            blackView.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(handleTap))) // Once tapped, calls handleDismiss to dismiss blackView
            
            window.addSubview(blackView)
            window.addSubview(collectionView) // add after blackView so it is in front
            
            let height: CGFloat = CGFloat(settings.count) * cellHeight
            let y = window.frame.height - height
            collectionView.frame = CGRect(x: 0, y: window.frame.height, width: window.frame.width, height: height) // Creates a white collection view to appear on the bottom of the screen
            
            
            blackView.frame = window.frame
            blackView.alpha = 0
            
            // Easy out curve - Animation accelerates in the beginning and slows in the end
            UIView.animate(withDuration: 0.5, delay: 0, usingSpringWithDamping: 1, initialSpringVelocity: 1, options: .curveEaseOut, animations: {
                self.blackView.alpha = 1      // Animates the blackView alpha from 0 to 1 in 0.5 seconds
                self.collectionView.frame = CGRect(x: 0, y: y, width: self.collectionView.frame.width, height: self.collectionView.frame.height) // Animates the collectionView's height from the view.height to var y
                
            }, completion: nil)
        }
        
    }
    
    
// Functions
//==============================================================================================================================================================================================================================================
    @objc func handleTap() {
        let newSetting = Setting(name: "", imageName: "")
        handleDismiss(setting: newSetting)
    }
    
    @objc func handleDismiss(setting: Setting) {
        UIView.animate(withDuration: 0.5, delay: 0, usingSpringWithDamping: 1, initialSpringVelocity: 1, options: .curveEaseOut, animations: {
            self.blackView.alpha = 0                       // Dismisses the blackView in 0.5 seconds
            if let window = UIApplication.shared.keyWindow {
                self.collectionView.frame = CGRect(x: 0, y: Int(window.frame.height), width: Int(window.frame.width), height: Int(window.frame.height))
            }
        }) {(completed: Bool) in
            if setting.name != "Cancel" && setting.name != "" {
                self.homeController?.showControllerForSetting(setting: setting)
            }
        }
    }
    
    // These two functions are to comform to UICollectionViewDataSource
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return settings.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath) as! SettingCell
        let setting = settings[indexPath.item]
        cell.setting = setting
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: collectionView.frame.width, height: cellHeight)
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
        return 0        // Changes the spacing between the cells
    }
    
    // When A button in settings is pressed
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        
        let setting = self.settings[indexPath.item]
        handleDismiss(setting: setting)
    }
    
    
    override init() {
        super.init()
        collectionView.delegate = self
        collectionView.dataSource = self
        
        collectionView.register(SettingCell.self, forCellWithReuseIdentifier: cellId)
        
    }
}
