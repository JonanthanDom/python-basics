import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  var pos = 0.0;
  final textController = TextEditingController();
  void calculo() {
    final resultado = (int.tryParse(textController.text) ?? 0) / 3;
    setState(() {
      pos = resultado;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16),
          child: Column(
            children: [
              SizedBox(height: 24),
              TextFormField(
                onChanged: (value) {
                  calculo();
                },
                controller: textController,
                keyboardType: TextInputType.phone,
                decoration: InputDecoration(label: Text('Ureia pré')),
              ),
              SizedBox(height: 24),
              Text(pos.toStringAsFixed(0)),
              SizedBox(height: 24),
              ElevatedButton(onPressed: calculo, child: Text('Calcular')),
            ],
          ),
        ),
      ),
    );
  }
}
