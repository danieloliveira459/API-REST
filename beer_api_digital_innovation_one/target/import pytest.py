import pytest
from fastapi import FastAPI # type: ignore

app = FastAPI()

# Estoque inicial de cerveja
estoque = {
    "cerveja_daniels": 50,
    "cerveja_ipa": 30,
    "cerveja_stout": 20
}
import static org.mockito.Mockito.*; # type: ignore
import static org.junit.jupiter.api.Assertions.*; # type: ignore
import org.junit.jupiter.api.BeforeEach; # type: ignore
import org.junit.jupiter.api.DisplayName; # type: ignore
import org.junit.jupiter.api.Test; # type: ignore
import org.mockito.InjectMocks; # type: ignore
import org.mockito.Mock; # type: ignore
import org.mockito.MockitoAnnotations; # type: ignore

public class BeerServiceTest { # type: ignore

    @Mock
    private BeerRepository beerRepository;

    @InjectMocks
    private BeerService beerService;

    private Beer validBeer;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.initMocks(this);
        validBeer = new Beer(1L, "IPA", "Heineken", 50, 10);
    }

    @Test
    @DisplayName("Deve adicionar cerveja ao estoque com sucesso")
    void shouldAddBeerSuccessfully() {
        // Given that the beer stock arrived
        when(beerRepository.save(any(Beer.class))).thenReturn(validBeer);

        // When  to return empty stock
        Beer beer = beerService.addBeer(validBeer);

        // Then  it will be taken to the distributor
        assertNotNull(beer);
        assertEquals("IPA", beer.getName());
        verify(beerRepository, times(1)).save(validBeer);
    }

    @Test
    @DisplayName("Deve lançar exceção ao adicionar uma cerveja com estoque negativo")
    void shouldThrowExceptionWhenAddingBeerWithNegativeStock() {
        // Given
        Beer invalidBeer = new Beer(2L, "Pilsner", "Brahma", -5, 10);

        // When / Then
        assertThrows(InvalidBeerStockException.class, () -> beerService.addBeer(invalidBeer));
    }
}

# Endpoint para resetar o estoque
@app.post("/estoque/resetar")
def resetar_estoque():
    estoque["cerveja_daniels"] = 50
    estoque["cerveja_ipa"] = 30
    estoque["cerveja_stout"] = 20
    return {"message": "Estoque resetado com sucesso", "estoque": estoque}
from fastapi.testclient import TestClient # type: ignore
from main import app  # type: ignore # supondo que a API está no arquivo main.py

client = TestClient(app)

def test_resetar_estoque():
    # Faz uma requisição POST para o endpoint de resetar estoque
    response = client.post("/estoque/resetar")
    
    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 200
    
    # Verifica o corpo da resposta
    data = response.json()
    assert data["message"] == "Estoque resetado com sucesso"
    
    # Verifica se os valores do estoque foram resetados corretamente
    assert data["estoque"]["cerveja_daniels"] == 50
    assert data["estoque"]["cerveja_ipa"] == 30
    assert data["estoque"]["cerveja_stout"] == 20
    pytest


