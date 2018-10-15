//
//  ViewController.swift
//  NewApp
//
//  Created by Jeffery Ho on 7/14/18.
//  Copyright © 2018 Jeffery Ho. All rights reserved.
//

import UIKit

class HomeController: UICollectionViewController, UICollectionViewDelegateFlowLayout {
    
    
// Constants
//==============================================================================================================================================================================================================================================
    let titles = ["Home", "Search", "Favorite", "Account"]
    let cellId = "cellId"
    let searchId = "searchId"
    let favoriteId = "favoriteId"
    let accountId = "accountCellId"
    
// Variables
//==============================================================================================================================================================================================================================================
    
    // Only ran once so it doesnt run unnecessariy repetitive code
    lazy var settingsLauncher: SettingsLauncher = {
        let launcher = SettingsLauncher()
        launcher.homeController = self
        return launcher
    }()
    
    lazy var menuBar: MenuBar = {
        let mb = MenuBar()
        mb.homeController = self
        return mb
    }()
    
    lazy var searchcell: SearchCellDetail = {
        let sc = SearchCellDetail()
        sc.homeController = self
        return sc
    }()

    
// Body
//==============================================================================================================================================================================================================================================
    override func viewDidLoad() {
        super.viewDidLoad()

        navigationItem.title = "Home"
        navigationController?.navigationBar.isTranslucent = false                       // Makes the navigation bar translucent
        navigationController?.navigationBar.layer.shadowColor = UIColor.black.cgColor
        navigationController?.navigationBar.layer.shadowOffset = CGSize(width: 1, height: 1)
        navigationController?.navigationBar.layer.shadowRadius = 2
        navigationController?.navigationBar.layer.shadowOpacity = 1
        navigationItem.setHidesBackButton(false, animated: false)
        
        let titleLabel = UILabel(frame: CGRect(x: 0 , y: 0, width: view.frame.width, height: 40))
        titleLabel.text = "Home"
        titleLabel.textColor = UIColor.black
        titleLabel.textAlignment = .center
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        titleLabel.superview?.addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .centerX, relatedBy: .equal, toItem: titleLabel.superview, attribute: .centerX, multiplier: 1, constant: 0))
        titleLabel.superview?.addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .width, relatedBy: .equal, toItem: titleLabel.superview, attribute: .width, multiplier: 1, constant: 0))
        titleLabel.superview?.addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .centerY, relatedBy: .equal, toItem: titleLabel.superview, attribute: .centerY, multiplier: 1, constant: 0))
        titleLabel.superview?.addConstraint(NSLayoutConstraint(item: titleLabel, attribute: .height, relatedBy: .equal, toItem: titleLabel.superview, attribute: .height, multiplier: 1, constant: 0))
        navigationItem.titleView = titleLabel
        
        
        setupCollectionView()
        setupMenuBar()
        setupNavBarButtons()
    }

    
// Functions
//==============================================================================================================================================================================================================================================
    
    func setupCollectionView() {
        collectionView?.backgroundColor = UIColor.white
        //collectionView?.register(IconCell.self, forCellWithReuseIdentifier: "cellId")
        self.collectionView?.isScrollEnabled = false
        //collectionView?.register(UICollectionViewCell.self, forCellWithReuseIdentifier: cellId)
        collectionView?.register(HomeView.self, forCellWithReuseIdentifier: cellId)
        // Makes the collection view, the videos, shift down 50, so its not under the navigation bar
        //collectionView?.contentInset = UIEdgeInsetsMake(80,0,0,50)
        
        // Makes the scroll 50 pixels lower so it doesn't go under the navigation bar
        //collectionView?.scrollIndicatorInsets = UIEdgeInsetsMake(50, 0, 0, 0)
        
        collectionView?.register(SearchView.self, forCellWithReuseIdentifier: searchId)
        collectionView?.register(FavoriteView.self, forCellWithReuseIdentifier: favoriteId)
        collectionView?.register(AccountView.self, forCellWithReuseIdentifier: accountId)
        
    }
    
    private func setTitle(index: Int) {
        if let titleLabel = navigationItem.titleView as? UILabel {
            titleLabel.text = "\(titles[index])"
            navigationItem.title = titleLabel.text
        }
    }
    
    // Adds functional navigation buttons to the navigation bar
    func setupNavBarButtons() {
        let moreButton = UIBarButtonItem(image: UIImage(named: "nav_more_icon")?.withRenderingMode(.alwaysTemplate), style: .plain, target: self, action: #selector(handleMore))
        let searchButton = UIBarButtonItem(image: UIImage(named: "search_icon")?.withRenderingMode(.alwaysTemplate), style: .plain, target: self, action: #selector(handleSearch))
        moreButton.tintColor = UIColor.rgb(red: 0, green: 0, blue: 0)
        searchButton.tintColor = UIColor.rgb(red: 0, green: 0, blue: 0)
        navigationItem.rightBarButtonItems = [moreButton, searchButton]
    }
    
    // This function is called when the more button is pressed
    @objc func handleMore() {
        settingsLauncher.showSettings()
    }
    
    // This function is called when the more button is pressed
    @objc func handleSearch() {
        settingsLauncher.showSettings()
    }

    func showControllerForSetting(setting: Setting) {
        let dummySettingViewController = UIViewController()
        dummySettingViewController.view.backgroundColor = UIColor.white
        dummySettingViewController.navigationItem.title = setting.name
        navigationController?.navigationBar.tintColor = UIColor.black
        navigationController?.navigationBar.titleTextAttributes = [NSAttributedStringKey.foregroundColor: UIColor.black]
        self.navigationController?.pushViewController(dummySettingViewController, animated: true)
    }
    
    func showBusinessController() {
        let dummySettingViewController = UIViewController()
        dummySettingViewController.view.backgroundColor = UIColor.white
        navigationController?.pushViewController(dummySettingViewController, animated: true)
    }
    
    func scrollToMenuIndex(menuIndex: Int) {
        setTitle(index: menuIndex)
        let indexPath = IndexPath(item: menuIndex, section: 0)
        collectionView?.scrollToItem(at: indexPath, at: [], animated: false)
    }
    
    private func setupMenuBar() {
        view.addSubview(menuBar)
        view.addConstraintsWithFormat(format: "H:|[v0]|", views: menuBar)
        view.addConstraintsWithFormat(format: "V:[v0(60)]|", views: menuBar)
    }
    
    override func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        print(indexPath.item)
       // if indexPath.item == 1 {
        //navigationController?.transition(from: HomeController, to: searchcell, duration: 0, options: [], animations: nil, completion: false)
        //}
    }
    
    // Number of section in menubar
    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 4
    }
    
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        

        switch indexPath.item {
        case 0: return collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath)
        case 1: return collectionView.dequeueReusableCell(withReuseIdentifier: searchId, for: indexPath)
        case 2: return collectionView.dequeueReusableCell(withReuseIdentifier: favoriteId, for: indexPath)
        case 3: return collectionView.dequeueReusableCell(withReuseIdentifier: accountId, for: indexPath)
        default: return collectionView.dequeueReusableCell(withReuseIdentifier: cellId, for: indexPath)
        }
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: view.frame.width, height: view.frame.height)
    }
    
    
}



class MyViewController: UIViewController, MyDelegate {
    
    var myView: MyView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        myView.delegate = self
    }
    
    func onButtonTapped() {
        let nextViewController = UIViewController()
        
        navigationController?.pushViewController(nextViewController, animated: false)
    }
}





