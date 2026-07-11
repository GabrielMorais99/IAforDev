var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();
builder.Services.AddHttpClient("ml-service", client =>
{
    client.BaseAddress = new Uri(
        builder.Configuration["Services:MachineLearning"] ?? "http://localhost:8000");
    client.Timeout = TimeSpan.FromSeconds(30);
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.MapGet("/health", () => Results.Ok(new
{
    status = "healthy",
    service = "AiForDevs.Api",
    timestamp = DateTimeOffset.UtcNow
}));

app.MapPost("/api/v1/classifications", async (
    ClassificationRequest request,
    IHttpClientFactory httpClientFactory,
    CancellationToken cancellationToken) =>
{
    if (request.Features is null || request.Features.Count == 0)
    {
        return Results.ValidationProblem(new Dictionary<string, string[]>
        {
            [nameof(request.Features)] = ["Informe pelo menos uma feature."]
        });
    }

    // Este endpoint começa como contrato de integração. Evolua-o nos laboratórios
    // para chamar o serviço Python, validar o schema e tratar falhas do provider.
    var client = httpClientFactory.CreateClient("ml-service");

    return Results.Accepted(value: new
    {
        requestId = Guid.NewGuid(),
        status = "integration-pending",
        mlService = client.BaseAddress,
        receivedFeatures = request.Features.Keys.OrderBy(key => key)
    });
});

app.Run();

public sealed record ClassificationRequest(Dictionary<string, object?> Features);
