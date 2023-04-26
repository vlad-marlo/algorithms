package main

import (
	"fmt"
)

type Input struct {
	Id         string `json:"$id"`
	Type       string `json:"type"`
	Properties struct {
		Id struct {
			Type        string `json:"type"`
			Description string `json:"description"`
		} `json:"id"`
		Price struct {
			Type        string `json:"type"`
			Description string `json:"description"`
		} `json:"price"`
		StockCount struct {
			Type        string `json:"type"`
			Description string `json:"description"`
		} `json:"stock_count"`
		PartnerContent struct {
			Type       string `json:"type"`
			Properties struct {
				Title struct {
					Type        string `json:"type"`
					Description string `json:"description"`
				} `json:"title"`
				Description struct {
					Type        string `json:"type"`
					Description string `json:"description"`
				} `json:"description"`
			} `json:"properties"`
		} `json:"partner_content"`
	} `json:"properties"`
	Required []string `json:"required"`
}

type Output struct {
	Id         string `json:"$id"`
	Type       string `json:"type"`
	Properties struct {
		TraceId struct {
			Type string `json:"type"`
		} `json:"trace_id"`
		Offer struct {
			Ref string `json:"$ref"`
		} `json:"offer"`
	} `json:"properties"`
	Required []string `json:"required"`
}

func main() {
	var n, m int
	if _, err := fmt.Scan(&n, &m); err != nil {
		panic(err)
	}

	for propertiesIndex := 0; propertiesIndex < m; propertiesIndex++ {

	}
	fmt.Print(n, m, "\n")
	//decoder := json.NewDecoder(os.Stdin)

}
