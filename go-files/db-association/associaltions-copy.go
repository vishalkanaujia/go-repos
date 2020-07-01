package main

import (
	"encoding/json"
	"fmt"

	"github.com/jinzhu/gorm"
	_ "github.com/lib/pq"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "postgres"
	password = ""
	dbname   = "postgres"
)

type Page struct {
	ID     int64  `sql:"auto_increment" json:"-"`
	Number int64  `json:"number"`
	Book   Book   `gorm:"foreignkey:book_id" json:"-"`
	BookID int64  `json:"book_id"`
	Text   string `json:"text"`
}

type Book struct {
	ID          int64  `sql:"auto_increment" json:"-"`
	ShelfPlace  int64  `json:"shelf_place"`
	Shelf       Shelf  `gorm:"foreignkey:shelf_id" json:"-"`
	ShelfID     int64  `json:"shelf_id"`
	Author      string `json:"author" gorm:"unique;not null"`
	Publisher   string `json:"publisher"`
	PagesAmount int64  `json:"pages_amount"`
	Pages       []Page `json:"pages"`
}

type Shelf struct {
	ID          int64  `sql:"auto_increment" json:"-"`
	Number      int64  `json:"number"`
	BooksAmount int64  `json:"books_amount"`
	Book        []Book `json:"books"`
}

func main() {
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)

	db, err := gorm.Open("postgres", psqlInfo)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	// Create
	//db.Create(&Shelf{
	record := `{
			"number": 1,
			"books": [
			  {
				"shelf_place": 5,
				"author": "Lewis Carroll",
				"publisher": "EA",
				"pages_amount": 2,
				"pages": [
				  {
					"number": 2,
					"text": "lorem ipsum"
				  },
				  {
					"number": 4,
					"text": "dolor sit amet"
				  }
				]
			  },
			  {
				"shelf_place": 7,
				"author": "Mark Twain",
				"publisher": "Activision",
				"pages_amount": 3,
				"pages": [
				  {
					"number": 1,
					"text": "this is"
				  },
				  {
					"number": 3,
					"text": "a test"
				  },
				  {
					"number": 6,
					"text": "of json"
				  }
				]
			  }
			]
		  }`
	var shelf Shelf

	err = json.Unmarshal([]byte(record), &shelf)
	fmt.Printf("err=%v\n", err)

	db.DropTableIfExists(&Shelf{})
	db.DropTableIfExists(&Page{})
	db.DropTableIfExists(&Book{})

	// Migrate the schema
	db.AutoMigrate(&Shelf{})
	db.AutoMigrate(&Page{})
	db.AutoMigrate(&Book{})

	//db.Create(&shelf)
	//db.Create(&shelf)

	db.Preload("Book").Where("author = ?", "Mark Twain").Find(&shelf)
	fmt.Printf("shelf=%v", shelf)
}
